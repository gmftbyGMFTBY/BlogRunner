# MockJS Document

MockJS 的作用是拦截AJAX请求并模拟生成随机数据返回给前端，实现我们的前端和后端开发的分离

## 安装和使用

```bash
# 安装
npm install mockjs
# 简单使用
<script src = "http://mockjs.com/dist/mock.js"></script>
# 项目工程使用 ....
```

## 语法

```javascript
// name 是属性名
// rule 是生成规则
// value 是属性值
// 生成规则可以有很多的形式
/* 
    'name|min-max': value
    'name|count': value
    'name|min-max.dmin-dmax': value
    'name|min-max.dcount': value
    'name|count.dmin-dmax': value
    'name|count.dcount': value
    'name|+step': value
*/
// 属性值还可以有不同形式
/*
    @占位符
    对象
*/
'name|rule' : value
```

 按照value的类型可以分成不同的形式

* String:

  属性值是字符串的时候代表重复min~max / count次

* Number:

  * +step : 初始值value上自动加step
  * min~max : 生成一个在min~max范围内和value同类型的数字
  * min~max.dmin~dmax : 整数部分同上，小数部分是保留在dmin~dmax位之间

* Boolean:

  * 1 : 生成value(true / false)的概率是0.5
  * min~max : 生成value(true / false)的概率是 `min / min + max`

* Object

  随机从Object中抽取count / min~max个属性

* Array:

  * 1 : 随机选取一个元素
  * min~max / count : 重复Array生成新数组

* RegExp:

  随机的反向生成正则表达式的对应的匹配字符串，用来自定义有格式的数据

## 函数接口

* 生成Mock对象

  ```javascript
  var Mock = require('mockjs')
  ```

* 生成模拟数据

  ```javascript
  // 对url的AJAX请求做拦截操作,字符串或者正则
  // type : get / post / put / delete 
  // function 是生成相应数据的函数
  // template就是我们的JSON对象，内部使用mockjs的语法
  Mock.mock(url , type , template | function(options));
  ```

* 配置拦截的参数

  ```javascript
  // settings : timeout
  // AJAX被拦截的响应时间，单位是毫秒
  Mock.setup({timeout: 400});
  Mock.setup({timout: '200-600'});    // 默认10-100
  ```

* Mock.Random工具类，用来生成各种随机数据

  1. **Mock.Random 的方法在数据模板中称为『占位符』，书写格式为 @占位符(参数 [, 参数]) **

     ```javascript
     var Random = Mock.Random
     Random.email()
     // => "n.clark@miller.io"
     Mock.mock('@email')
     // => "y.lee@lewis.org"
     Mock.mock( { email: '@email' } )
     // => { email: "v.lewis@hall.gov" }
     ```

  2. 函数集合

     * `Random.boolean`(min , max , current) :

        current(true / false)出现的概率是`min / min + max` 

     * `Random.natural(min , max)`:

       返回一个随机的自然数，在min~max之间

     * `Random.integer(min , max)`:

       同上

     * `Random.float(min , max , dmin , dmax)`:

       同上

     * `Rancom.character(pool)`:

       pool是一个字符池，将从中选取字符返回

       * 内置的字符池

         ```javascript
         {
             lower: "abcdefghijklmnopqrstuvwxyz",
             upper: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
             number: "0123456789",
             symbol: "!@#$%^&*()[]"
         }
         ```

       如果没有自定义字符池，那么会从上面的所有字符中随机的选择一个，否则从用户提供的字符池中随机的选取一个返回

     * `Random.string(pool ,min , max)`:

       1. pool同上
       2. min~max / length:随机字符串的长度约束

     * `Random.range(begin , end , step)`:

       返回整型数组，同Python语法

     * ``Random.date(format)`:

       按照format字符串生成对应的随机时间格式,一般常用是'yyyy-MM-dd' / 'yy-MM-dd'

     * `Random.time(format)`:

       生成一天内的时间，一般常用format是null / 'A HH:mm:ss' / 'HH:mm:ss'

     * `Random.datetime(format)`:

       上述的混合，format也是

     * `Random.now(unit , format)`:

       unit用来进行格式化

       * year : 除了年份以外数据格式化
       * month : 除了年月以外格式化
       * week : 除了年月星期以外格式化
       * day : 除了年月日以外格式化
       * hour : 除了年月日小时以外格式化
       * minute : ...
       * second : ...

     * `Random.image(size , background , forehead , format , text)`:

       生成一个随机的图片地址。

       * size : 图片的大小，默认从下种随机选取

         ````javascript
         [
             '300x250', '250x250', '240x400', '336x280', 
             '180x150', '720x300', '468x60', '234x60', 
             '88x31', '120x90', '120x60', '120x240', 
             '125x125', '728x90', '160x600', '120x600', 
             '300x600'
         ]
         ````

       * background : 图片的背景色

       * forehead : 图片的前景色

       * format : 图片的格式

       * text : 图片的文字

     * `Random.color() / Random.hex() / Random.rgb() / Random.rgba() / Random.hsl()` :

       随机生成有吸引力的颜色

     * `Random.paragraph(min , max)`:

       随机生成文本

       句子的个数在length / min~max

     * `Random.cparagraph(min , max)`:

       随机生成中文文本

     * `Random.sentence(min , max)`:

       随机生成一个句子，第一个单词的首字母大写

       length / min~max之间的单词

     * `Random.csentence(min , max)`:

       随机生成中文的文本

       length / min~max之间的字的个数

     * `Random.word(min , max)`:

       随机生成一个单词

       length / min~max 个字符的个数

     * `Random.cword(pool , min , max)`:

       length / min~max : 汉子字符串的长度

     * `Random.first() / Random.last() / Random.name(middle) / Random.cfirst() / Random.clast() / Random.cname()`

       middle决定是够生成中间名

     * `Random.url(protocol , host) / Random.protocol() / Random.domain() / Random.email() / Random.ip()`:

       ```javascript
       Random.url()
       // => "mid://axmg.bg/bhyq"
       Random.url('http')
       // => "http://splap.yu/qxzkyoubp"
       Random.url('http', 'nuysoft.com')
       // => "http://nuysoft.com/ewacecjhe"
       ```

     * `Random.region() / Random.province() / Random.city(prefix) / Random.county(prefix) / Random.zip()`:

       prefix决定是否将上级省市打印出来

       ​