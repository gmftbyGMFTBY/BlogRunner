## I Overview

### 1.Project Goal

* 项目基于Python3.6开发
* 博客爬取软件
* 引入多种爬取思路
  * 用户 + 博客官网爬取
  * 语义爬取
  * 信息抽取和摘要生成
* 后端数据提供前端信息反馈

### 2.The key for this project

本仓库中的项目内容是BIT 2017~2018学年度第一学期软件工程科目的时实践考查课

本项目需要的基础知识和技能如下

* MySQL5.4

  团队使用 `pymysql` / `Sqlalchemy` 构建Python核心代码和MySQL数据库的连接

* Scrapy1.4

  团队使用 `Scrapy1.4` 的 `Python` 爬虫框架网络爬取相关数据并存储在本地的数据库中以供之后的数据分析和智能识别从数据中抽取出重要或者对用户友好的信息以返回给前端

* B / S 

  前端后端设计开发

  * `Ajax` : 异步JS和XML
  * `JSON` : JavaScript对象表示法最为前后端的文本传输交换的数据格式
  * `elementUI` + `VNE2.0` : 前端轻量级CSS / JS框架
  * `Mockjs` : 对前端开发和后端开发的分离，截取并模拟相应Ajax数据以便返还检验前端设计
  * `JavaScript` : 前端设计构建

  ---

  * `Python3.6`
    * `Scrapy1.4`
    * `Flask` : 后端采用轻量级Python Web框架Flask
    * `Numpy` : 科学计算库对数据进行抽取和分析
    * `NLTK` : Python自然语言处理模块实现简单语义分析

### 2.The member and division of labour

#### Member and Jobs

* 兰天     : Tian Lan

  后端设计和开发,爬虫搭建,数据分析编码等

* 雷亚洲 : Yazhou Lei

  前端设计和开发

* 李继领 : Jiling Li

  前端设计和开发


* 李智强 : Zhiqiang Li

  数据库设计和构建

* 郭莹婷 : Yingting Guo

  运行测试

#### Division of labour

* 组长 : 兰天

### 3.The essential metadata of Team

* 组名:

  English : Blog Pedestrain

  Chinese : 博客行者

* Logo:

  ![BlogPedestrain](/home/lantian/File/Software-Engine/Sources/Photo/BlogPedestrain.png)

### 4.Requirement analysis

* 需求构想

  作为计算机学院的学生，上网查询技术博客已经成为我们的频繁习惯。

  但是每一次我们在`Bing` / `Google` / `Baidu`上的检索都会得到失望的结果，理由大致如下

  * 我们都是在一篇一篇的翻阅博客，经常会乱糟糟的毫无头绪或者说最终失望而归
  * 感觉找到了一位好博主的系列文章但却苦于文章过多且目录混杂难以下手
  * 优秀的开发文档但是需要我们一篇一篇的摘取和收藏非常的繁琐
  * 某搜索引擎的广告过于烦人影响阅读心情
  * 文章选择过多无从下手

  所以我萌发了制作一个博客爬虫的构想，便捷**本人**和**其他的学习计算机基础学科**或者**其他学科**的同学以便快速的查阅相应的技术博客和开发信息

* 需求分析

  * 定向爬取博客和技术论坛

    定向爬取博客的核心内容在于我们约束的几点爬取策略

    1. 基于用户的博客平台的爬取

       用户指定需要爬取的**博主**的博客平台(cnblog / CSDN / 开源中国 / IBM developerWorks / Segementfault)

       1. 可以选择是否继续指定爬取的关键点，以便更有目的的爬取文章
       2. 如果没有继续指定则默认爬取该博主在某一个指定的博客平台的所有技术文档(如果技术文档数目过于庞大，可以选择按照优先级排序显示某几个,这一点需要**文章筛选策略**的支持)

       Input : 

       * 用户账号
       * 博客平台
       * 技术关键字

    2. 基于关键字的爬取

       用户指定某一个**技术关键字**，后台爬虫在指定的搜索引擎中有目的的寻找和筛选(需要**文章筛选策略**的支持)

       Input :

       - 技术关键字
       - 主流搜索引擎

    3. 基于URL的爬取

       用户可以制定我们要爬取的HTML网页的URL，我们可以提供本地序列化和导出的功能

  * 相关信息导航

    1. 利用百度 , WIKI等百科词条搜索和用户指定的技术关键字的有关的相关信息并在前端页面中进行显示
    2. 不建议对导航结果进行序列化，随着用户的搜索动态的变更

  * 文章筛选策略

    文章筛选策略，按照制定的几点筛选标准对已经抓取到的技术博客进行综合考量进而给出用户的**浏览优先级**，按照优先级排序并在前端显示给用户

    1. 留言筛选策略 : 

       如果可以定位到抓取的目标中的留言的话，对留言全方位考虑评判文章

       * 留言敏感词汇

         ```
         垃圾 ， 没有 ， 谢谢 ， 感谢 ， 膜拜 ， 大佬 ， 错误 ， 收藏 ...
         ```

         这里需要AI / 自然语言处理的相关技术支持

       * 留言条目数量

    2. 技术关键字次数捕捉策略

       如果用户指定了技术关键字，我们可以根据文章中出现的技术关键字的次数对文章的效果进行基本评价

    3. 文章篇幅策略

       对文章的篇幅实现文章过滤，满足不同的用户的搜索过滤要求

    4. 文章查重

       因为大量存在博客剽窃和转载的情况，我们对爬取的博客需要进行去重操作降低爬取数据的冗余

  * 分布式爬虫

    `TO BE CONTINUE ...`

  * 用户自定义

    1. 搜索引擎的选取

    2. 自定义爬取列表

       用户可以制定爬取的系列文章和网页文档的源代码的描述，方便我们聚焦搜索源头

       * 正文HTML标签
       * 评论HTML标签
       * 题目HTML标签

    3. 本次搜索是否保存在本地数据库

  * 本地序列化

    **数据库支持**

    1. 用户一旦要将搜索结果保存在数据库，需要制定本次的**保存的关键字**和**有效日期**
    2. 用户决定是否将数据库中的内容导出到电脑上以便打印
    3. 搜索历史查询
    4. 数据库制定触发器对大表的**按时间的删除修正**和**数据库还原**

* 预计开发耗时

  * 资料收集和消化学习 : 7 ~ 10 days
  * 代码编写 : 10 ~ 20 days

---

## II Flow of Development

### 1.Document Collection

* 截止日期 : 2017.9.19 ~ 2017.9.25
* 组员文档

**TO BE CONTINUED ...**

