# Scrapy Document

## 初窥Scrapy

1. scrapy用来爬取结构化数据，应用广泛
2. 支持网页爬取，和API爬取
3. 异步方式调度和处理我们的爬虫，某一个请求及时失败了其他的请求还会继续运行
4. 需要认识到scrapy异常强大
   * 内置支持使用CSS选择器和XPath表达式提取数据，当然你要使用bs4也是可以的
   * 拥有交互式的控制台换几个，类似于IPython,用于检验我们的爬虫的可靠性和正确性
   * 内置支持多种文件导出格式，不必自己`import json , csv `浪费精力
   * 强大的编码检验支持，自动检测
   * 可扩展性，自定义性强(API定义良好)
   * 中间件支持
     * cookies
     * http压缩
     * 爬取深度约束

## 安装指南

1. pip

   ```bash
   pip install Scrapy
   # 当然也可以使用Anaconda
   conda install -c scrapinghub scrapy
   ```

2. 了解

   * Scrapy是Python编写的，需要依赖包如下
     * lxml : HTML解析器
     * parsel : 在lxml上的数据提取库
     * w3lib
     * twistes
     * pyOpenSSL ...

## Scrapy教程

我们教程的爬取目标是`quotes.toscrape.com`一个列出了名人名言的网站

### 创建Scrapy项目

1. 创建项目

   ```bash
   scrapy startproject project_name
   ```

   创建的项目目录

   ```bash
   .
   ├── scrapy.cfg            # 配置文件
   └── tutorial
       ├── __init__.py
       ├── __pycache__
       ├── items.py          # item定义文件
       ├── middlewares.py    # 中间件定义文件
       ├── pipelines.py      # 管道定义文件
       ├── settings.py       # 设置定义文件
       └── spiders           # 爬虫定义文件
           ├── __init__.py
           └── __pycache__
   ```

### 创建Spider类

1. Spider是由你定义的,是用来从一个网站（或一组网站）爬取信息的类。它们必须继承`scrapy.Spider`然后定义发出的初始请求，可以选择定义跟踪页面中的链接，以及如何解析下载页面的内容来提取数据。

2. 在Spiders文件加下创建一个test.py文件

   ```python
   import scrapy

   class QuotesSpider(scrapy.Spider):    # 必须继承自scrapy.Spider
       name = "quotes"

       def start_requests(self):
           urls = [
               'http://quotes.toscrape.com/page/1/',
               'http://quotes.toscrape.com/page/2/',
           ]
           for url in urls:
               yield scrapy.Request(url=url, callback=self.parse)

       def parse(self, response):
           page = response.url.split("/")[-2]
           filename = 'quotes-%s.html' % page
           with open(filename, 'wb') as f:
               f.write(response.body)
           self.log('Saved file %s' % filename)
   ```

   * name : 标识一个Spider,在项目中必须唯一

   * start_request : 必须返回一个Request的可迭代对象(列表或者生成器),Spider之后将会爬取他们，后续的请求也有他们生成

   * parse : 

     0. 默认的回调方法
     1. 处理解析下载的文件的数据，response参数保留爬取的页面的内容并提供访问这些内容的
     2. 解析的结果要么保存，要么生成新的Request返回之后爬取



### 运行爬虫

1. 回到项目的顶层，执行

   ```bash
   scrapy crawl quotes    # 运行新添加的爬虫(name属性唯一)
   ```

2. 执行细节

   * Scrapy调度爬虫的start_requests方法返回的scrapy.Request对象
   * 创建Response对象
   * 将Response传递给parse函数

3. 简化

   * 我们可以胜率start_requests函数调用默认的方法，将url包装成Request请求对象

     ```python
     import scrapy

     class QuotesSpider(scrapy.Spider):
         name = "quotes"
         start_urls = [
             'http://quotes.toscrape.com/page/1/',
             'http://quotes.toscrape.com/page/2/',
         ]

         def parse(self, response):
             page = response.url.split("/")[-2]
             filename = 'quotes-%s.html' % page
             with open(filename, 'wb') as f:
                 f.write(response.body)
     ```

4. 提取数据

   尝试在控制台试错式的提取数据

   ```bash
   scrapy shell 'http://quotes.toscrape.com/page/1/'    # 必须加引号
   ```

   生成IPython的解释器控制台，可以在这里对我们的提取的结果进行检验,在控制台县的常用的检验的方式

   * CSS

     ```python
     response.css('title').extract()    # 抽取HTML文本
     response.css('title').extract_first()
     response.css('title').re(r'Quotes.*')    # 提取HTML文档中的所有的匹配信息
     view(response)    # 在浏览器中打开我们爬取的页面，利用Firebug等查找需要的元素
     ```

   * XPath

     XPath表达式异常强大，基本上可以代替CSS选择器

     ```python
     response.xpath('//title')
     response.xpath('//title/text()').extract_first()
     ```

   在我们在shell中测试完我们提取数据的方式之后，下一步就是将这些方式集成到parse函数中



```python
import scrapy
class QuotesSpider(scrapy.Spider):   
   name = "quotes"
   start_urls = [
       'http://quotes.toscrape.com/page/1/',
       'http://quotes.toscrape.com/page/2/',
   ]

   def parse(self, response):
       for quote in response.css('div.quote'):
           yield {
               'text': quote.css('span.text::text').extract_first(),
               'author': quote.css('span small::text').extract_first(),
               'tags': quote.css('div.tags a.tag::text').extract(),
           }
```
5. 存储爬取的数据

   1. 默认是将结果保存起来或者打印到标准输出

   2. 但是我们对于标准输出的结果可以指定保存格式

      并且总是追加并不覆盖，建议手动删除后创建序列化文件

      ```bash
      scrapy crawl quotes -o quotes.json
      ```

   3. pipeline中存储我们的数据

6. 跟踪连接

   只需要提供种子url剩下的链接的跟踪自动完成

   1. 这里你看到的是Scrapy跟踪链接的机制︰当你在回调方法中yield一个Request，Scrapy将调度发送这个Request并注册一个在Request完成时执行的回调方法。
   2. callback函数支持我们自定义跟踪连接的方式

   ```python
   import scrapy

   class QuotesSpider(scrapy.Spider):
       name = "quotes"
       start_urls = [
           'http://quotes.toscrape.com/page/1/',
       ]

       def parse(self, response):
           for quote in response.css('div.quote'):
               yield {
                   'text': quote.css('span.text::text').extract_first(),
                   'author': quote.css('span small::text').extract_first(),
                   'tags': quote.css('div.tags a.tag::text').extract(),
               }

           next_page = response.css('li.next a::attr(href)').extract_first()
           if next_page is not None:
               next_page = response.urljoin(next_page)    # 利用urljoin生成完整的绝对路径去往下一页的请求
               yield scrapy.Request(next_page, callback=self.parse)    # 将自己注册成为回调函数，保证我们下一次还是使用parse来对这个请求进行处理和提取数据
   ```

7. 更多的例子

   1. Scrapy会自动的过滤掉URL的重复其扭曲

   ```python
   import scrapy

   class AuthorSpider(scrapy.Spider):
       name = 'author'

       start_urls = ['http://quotes.toscrape.com/']

       def parse(self, response):
           # 每一页的作者信息的链接标签求情使用parse_author来解析
           for href in response.css('.author a::attr(href)').extract():
               yield scrapy.Request(response.urljoin(href),
                                    callback=self.parse_author)

           # 下一页的跟踪继续使用parse来解析
           next_page = response.css('li.next a::attr(href)').extract_first()
           if next_page is not None:
               next_page = response.urljoin(next_page)
               yield scrapy.Request(next_page, callback=self.parse)

       def parse_author(self, response):
           def extract_with_css(query):
               return response.css(query).extract_first().strip()

           yield {
               'name': extract_with_css('h3.author-title::text'),
               'birthdate': extract_with_css('.author-born-date::text'),
               'bio': extract_with_css('.author-description::text'),
           }
   ```

8. Spider的参数

   a参数用来设置命令行参数，可以使用`self.`获取命令行参数

   ```bash
   scrapy crawl quotes -o quotes-humor.json -a tag=humor
   ```

## 基本操作

1. 创建新的Spider

   ```bash
   scrapy genspider spider_name domain_name
   ```

2. 创建项目

   ```bash
   scrapy startproject project_name
   ```

3. 运行爬虫

   ```bash
   scrapy crawl spider_name
   ```

4. 爬虫检查

   ```bash
   scrapy check 
   ```

5. 罗列可用爬虫

   ```bash
   scrapy list
   ```

6. 编辑爬虫

   ```bash
   scrapy edit spider_name
   ```

7. 调试模式

   ```bash
   scrapy shell "url"
   ```

## Spiders

1. Spiders是定义如何抓取某个网站（或一组网站）的类，包括如何执行抓取（即跟踪链接）以及如何从其网页中提取结构化数据（即爬取项目）。换句话说，Spider是你定义用于为特定网站（或在某些情况下，一组网站）抓取和解析网页的自定义行为的地方

2. 运行周期

   1. 以生成抓取第一批URL的初始请求开始，并指定一个回调函数，用于对这些请求下载的响应进行调用。

      第一批请求通过调用[`start_requests()`](http://www.usyiyi.cn/documents/scrapy_12/topics/spiders.html#scrapy.spiders.Spider.start_requests)方法（默认情况下）获得，这个方法为[`start_urls`](http://www.usyiyi.cn/documents/scrapy_12/topics/spiders.html#scrapy.spiders.Spider.start_urls)中指定的URL生成[`Request`](http://www.usyiyi.cn/documents/scrapy_12/topics/request-response.html#scrapy.http.Request)并为这些Request生成[`parse`](http://www.usyiyi.cn/documents/scrapy_12/topics/spiders.html#scrapy.spiders.Spider.parse)方法作为回调函数。

   2.  在回调函数内分析返回的(网页)内容，返回 [`Item`](http://www.usyiyi.cn/documents/scrapy_12/topics/items.html#scrapy.item.Item) 对象或者 [`Request`](http://www.usyiyi.cn/documents/scrapy_12/topics/request-response.html#scrapy.http.Request) 或者一个包括二者的可迭代容器。  返回的Request对象之后会经过Scrapy处理，下载相应的内容，并调用设置的callback函数(函数可相同)。 

   3.  在回调函数内，您可以使用 [选择器(Selectors)](http://www.usyiyi.cn/documents/scrapy_12/topics/selectors.html#topics-selectors) (您也可以使用BeautifulSoup, lxml 或者您想用的任何解析器) 来分析网页内容，并根据分析的数据生成item。 

   4.  最后，由spider返回的item将被存到数据库(由某些 [Item Pipeline](http://www.usyiyi.cn/documents/scrapy_12/topics/item-pipeline.html#topics-item-pipeline) 处理)或使用 [Feed exports](http://www.usyiyi.cn/documents/scrapy_12/topics/feed-exports.html#topics-feed-exports) 存入到文件中。 

3. 核心类 :

   `scrapy.Spider`只提供默认的下载方式和送往parse函数解析

   * name : 唯一的字符串(为了定位)
   * allowed_domains: 爬取的域名的列表
   * start_urls : 初始的URL列表
   * start_request : 默认的爬取的函数
   * parse : 提取数据和后续的Request , 返回Item / Request对象

4. 通用爬虫类

   1. Scrapy附带一些有用的通用spiders ，你可以使用它来子类化你的spiders。它们的目的是为几个常见的爬取案例提供方便的功能，例如根据某些规则查看网站上的所有链接，从[站点地图抓取](http://www.sitemaps.org)或解析XML/CSV Feed。

   2. 常见

      * `CrawlSpider`

        除了从`Spider`中集成的属性，支持新的特性

        ---

        * 首先引入scrapy.spiders.Rule类

          ​

          ---

          ​

          ​