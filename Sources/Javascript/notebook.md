# 一.JavaScript入门

## 1.什么是JavaScript

* 定义
  1. JavaScript是轻量级的编程语言
  2. JavaScript是可插入的HTML页面的编程代码
  3. JavaScript插入HTML页面后，可以被现代的浏览器执行
* 简单使用

1. HTML输出

   ```javascript
   document.write("....");
   ```

2. 弹窗

   ```javascript
   // alert()函数可以弹窗，便于测试代码
   // onclick是基础事件
   <button type="button" onclick="alert('Welcome!')">点击这里</button>
   ```

3. 更改HTML内容

   ```javascript
   x = document.getElementById("demo")  //查找元素，以id属性查找我们的HTML元素
   x.innerHTML = "Hello JavaScript";    //改变内容
   ```

4. 更改HTML图像

   JavaScript 能够改变任意 HTML 元素的大多数属性，而不仅仅是图片。

   ```javascript
   function changeImage()
   {
   element=document.getElementById('myimage')   //用id获取对应的HTML元素
   if (element.src.match("bulbon"))    //是否匹配到了对应的字符
     {
     element.src="/i/eg_bulboff.gif";
     }
   else
     {ent.getEleme
     element.src="/i/eg_bulbon.gif";
     }
   }
   ```

5. 改变HTML样式

   ```javascript
   function myFunction()
   {
       x=document.getElementById("demo") // 找到元素
       x.style.color="#ff0000";          // 改变样式
   }
   ```

6. 验证数字

   ```javascript
   function myFunction()
   {
   var x=document.getElementById("demo").value;    //获取input标签的数据
   if(x==""||isNaN(x))    //空或者不是数字，弹窗
   	{
   	alert("Not Numeric");
   	}
   }
   ```


## 2.JavaScript实现

1. JS脚本的存放位置

   * <script></script>标签内
   * <script>标签必须防止在我们的<head> / <body>标签中
   * 外部文件

2. <script>

   <script>标签嵌入在HTML中，指定我们的JS代码的开始和结束

3. 实例

   1. JS语句会在我们加载页面的时候进行执行
   2. 将JS代码加入函数充当事件
   3. HTML文档中的JS代码的标签数目是没有限定的，脚本可以同时存在与我们的<body> / <head>标签中的任何位置，**通常做法是放置在<head>标签中防止干扰页面**

   * <script> in <body>

     ```HTML
     <!DOCTYPE html>
     <html>
     <body>

     <p>
     JavaScript 能够直接写入 HTML 输出流中：
     </p>

     <script>
     document.write("<h1>This is a heading</h1>");
     document.write("<p>This is a paragraph.</p>");
     </script>

     <p>
     您只能在 HTML 输出流中使用 <strong>document.write</strong>。
     如果您在文档已加载后使用它（比如在函数中），会覆盖整个文档。
     </p>

     </body>
     </html>
     ```

   * <scripy> in <head>

     充当事件函数

     ```HTML
     <!DOCTYPE html>
     <html>
     <head>
     <script>
     function myFunction()
     {
     document.getElementById("demo").innerHTML="My First JavaScript Function";
     }
     </script>
     </head>

     <body>

     <h1>My Web Page</h1>

     <p id="demo">A Paragraph.</p>

     <!--点击的时候触发函数-->
     <button type="button" onclick="myFunction()">点击这里</button>

     </body>
     </html>
     ```

   * 外部JS脚本

     ```html
     <!DOCTYPE html>
     <html>
     <head></head>
     <body>
     <h1>My Web Page</h1>
     <p id="demo">A Paragraph.</p>
     <button type="button" onclick="myFunction()">点击这里</button>
     <script src = "./myscript.js"></script>
     </body>
     </html>
     ```

     ```javascript
     function myFunction()
     {
         document.getElementById("demo").innerHTML="My First JavaScript Function";
     }
     ```

## 3.JavaScript输出

JavaScript通常用来操作HTML元素

1. 获取HTML元素

   ```javascript
   // 以id获得对应的HTML元素
   document.getElementById("demo").innerHTML="My First Pharagh of JavaScript";
   ```

   JavaScript是用Web浏览器来执行的，对应的元素访问我们使用HTML来进行访问

2. 输出HTML元素

   ```javascript
   document.write("Something in here!")
   //注意我们的该函数事项文档书写内容，如果已经加载完文档知乎整个文档会被重新的书写
   ```

## 4.JavaScript语句

1. JavaScript 语句向浏览器发出的命令。语句的作用是告诉浏览器该做什么。

   e.g.

   ```javascript
   // 下面的 JavaScript 语句向 id="demo" 的 HTML 元素输出文本 "Hello World"：
   document.getElementById("demo").innerHTML="Hello World";
   ```

2. 分号

   1. 分号用来分割我们的JS语句
   2. 但是在JS中使用分好来分割语句是可选的方案

3. 所谓的JS代码

   JavaScript 代码（或者只有 JavaScript）是 JavaScript 语句的序列。

   浏览器会按照编写顺序来执行每条语句。

4. 所谓JS代码块

   函数是代码块的一种实现方式

   ```javascript
   function myfunction()
   {
     document.getElementById("demo").innerHTML="Hello World";
     document.getElementById("myDIV").innerHTML="How are you?";
   }
   ```

5. 大小写敏感

6. 忽略空格，但是可以空格来增加代码的可读性

7. 文本块折行

   **只可以对我们的文本字符串是用 \ 来进行折行，但是对代码不允许使用**

   ```javascript
   // Yes!
   document.write("Hello \
   World!");

   // No!
   document.write \
   ("Hello World!");
   ```


## 5.JavaScript注释

```javascript
// 单行注释
/* 多行注释 */
```

## 6.JavaScript变量

1. 声明变量

   ```javascript
   var x = 2;
   var y = 3;
   var z = x + y;
   var name = 'lantian';
   var Name = "GMFTBY";

   //一条语句多个变量
   var a = 1 , b = 2 , c = 3;
   ```

2. 数据类型

   JS是动态类型语言，一个变量可以拥有不同的类型

   * 数字 : 数字可以带小数点也可以不带小数点，支持科学计数法

     ```javascript
     var x = 123e5;    // 12300000
     ```

   * 字符串 : 双引号或者单引号括起来的任意文本

   * `undefined` : 

     **变量不含有值，**无值的变量，没有值的变量默认都是`undefined`

     ```javascript
     var name;    //name是undefined
     ```

     可以设置` null `来清空变量的值

     ```javascript
     var name = 'lantian';
     name = null;
     ```

   * 布尔变量

     * true
     * false

   * 数组

     数组下标是基于0的

     ```javascript
     var cars = new Array();
     cars[0] = 'lantian';
     cars[1] = 'GMFTBY';

     // OR
     var cars_new = new Array('lantian' , 'GMFTBY');

     // OR
     var cars_newp = ['lantian' , 'GMFTBY'];
     ```

   * 对象

     类似于Python的字典，用花括号区分，其间使用键值对的形式定义

     1. 声明

        ```javascript
        var person = {firstname : "lantian" , lastname : 'GMFTBY' , id ： 5505};
        ```

     2. 元素引用

        ```javascript
        name = person.lastname;
        name = person['lastname'];
        ```

   动态申请类型

   **JS的所有的比那辆都是对象，声明变量就相当于是创建对象**

   ```javascript
   var carname = new String;
   var x = new Number;
   var y = new Boolean;
   var cars = new Array;
   var person = new Object;
   ```

## 7.JavaScript对象

1. JS的对象是拥有属性和方法的数据

   ```javascript
   car.wheel = 'iron';
   car.drive();
   ```

2. 简单的例子

   字符串对象的使用

   ```html
   <html>
     <head>
     </head>
     <body>
       <p id = 'demo'></p>
       <script>
         var car = 'newcar';
         x = document.getElementById('demo');
         x.innerHTML = car.length;
         <!-- length是car的属性 -->
       </script>
     </body>
   </html>
   ```

3. 创建自己的对象

   ```javascript
   person = new Object();
   // 不断的项存在的对象中添加属性和方法
   person.firstname = 'bill';
   person.lastname = 'gates';
   person.age = 56;
   person.eyecolor = 'blue';
   ```

4. 访问对象属性和方法

   ```javascript
   var message = 'Hello World!';
   var x = message.toUpperCase();    //访问方法
   var length = message.length;    //访问属性
   ```

## 8.JavaScript函数

1. 函数是可以由**事件驱动**的或者**调用时执行的重用代码块**

2. 语句体

   ```javascript
   function functionname(arg1 , arg2 , ...)
   {
     // the code ...
     return ...;    // 返回值可以不存在，表示中断函数
   }
   ```

3. 变量作用域

   * 局部变量 : 
     1. 在函数中声明的变量只在函数内部可见
     2. 生存周期维持到函数结束
   * 全局变量 : 
     1. 在函数外声明的变量全局可见，网页所有的脚本和函数都可以进行访问
     2. 生存周期维持到页面关闭

## 9.JavaScript运算符

1. 运算符

   ```javascript
   + , - , * , / , % , ++ , -- , = , += , -= , *= , /= , %=
   ```

2. 特例执行

   ```javascript
   text1 = "xiaozi";
   text2 = "yuan";
   text3 = text1 + text2;
   ```

   **数字和字符串相加，结果变成字符串**

## 10.JavaScript逻辑运算符

1. 测试使用true / false

2. 条件运算符号

   ```javascript
   == (等于) , === (值和类型全等) ， ！= ， > , < , >= , <=
   ```

3. 逻辑运算符号

   ```javascript
   && , || , !
   ```

4. 三元运算符号

   ```javascript
   greeting = (visitor == 'pres')?"dear president":'dear';
   ```

## 11.JavaScript流程语句

```javascript
/*
if / if...else... / if...else if...else... / switch 
*/
if(...)
{
    // ...     
}

// else
if()
{
  // ...
}
else
{
  // ...
}

// else if
if()
{
  // ...
}
else if()
{
  // ...
}
else
{
  // ...
}

// switch
switch()
{
  case 1 : 
    // ...
    break;
  case 2 :
    // ...
    break;
  default:
    // ...
}

/*
for / while
*/
for(var i = 0 , len = cars.length;i < cars.length;i++)
{
  // ...
  break;
  continue;
}

var person = {fname:'lantian' , lname : 'GMFTBY'};
for(x in person)    //循环遍历我们的对象的每一个元素
  {
    text = text + person[x];
  }

while()
  {
    // ...
  }

/*
JavaScript的标签操作
使用标签先定义组代码块，然后在其中我们的break语句可以从任何位置跳出
*/
labelname :
{
  // ...
  // ...
  // ...
  // ...
  break labelname;    //跳出labelname的代码块
  // ...
}
```

## 12.JavaScript错误

1. JS代码执行的时候会出现各种各样的错误，我们需要错误机制来对不同的错误进行处理

2. 当程序出现问题的时候，JS的引擎会停止并抛出一个异常

3. 语法体

   ```javascript
   try
   {
     // ..这里可能会出现错误
   }
   catch(err)
   {
     // ..这里捕捉错误并处理,err是我们抛出的异常
   }
   ```

4. `throw`

   * 抛出异常

   * 异常可以使任何的JavaScript的对象(String , Number , Boolean , Object)

     err是我们抛出的异常，以便我们之后对接收的异常信息进行判断和分析处理


# 二.JavaScript DOM

## 1.DOM

1. `DOM`全称是文档对象模型

2. 当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model），HTML DOM 模型被构造为对象的树。

   ![DOM HTML 树](http://www.w3school.com.cn/i/ct_htmltree.gif)

3. JS对DOM可以做什么

   * 改变所有的HTML元素
   * 改变所有的HTML属性
   * 改变所有的CSS样式
   * 对事件做出反应

4. 查找到元素

   **注意所有的查询都是在当前的文档节点之下的，如果搜引导的节点不唯一，将会是一个数组可以使用编号索引到**

   * ID

     ```javascript
     var x = document.getElementById('intro');
     ```

   * 标签名

     ```javascript
     var x = document.getElementByTagName("p");   //查找p标签
     ```

   * 类名

## 2.DOM 改变 HTML

1. 改变HTML输出流，创建动态的HTML网页

   ```javascript
   <!DOCTYPE html>
   <html>
   <body>

   <script>
   document.write(Date());
   </script>

   </body>
   </html>
   ```

2. 修改**文档元素**的内容

   ```javascript
   document.getElementById("p1").innerHTML="New text!";
   ```

3. 改变HTML元素的属性

   ```javascript
   <img id="image" src="smiley.gif">

   <script>
   document.getElementById("image").src="http://www.w3school.com.cn/i/ct_htmltree.gif";
   </script>
   ```

## 2.DOM 改变 CSS

1. 样式修改

   ```javascript
   document.getElementById(id).style.property = new style;
   document.getElementById(id).style.color = 'blue';
   document.getElementById(id).style.visibility = 'hidden';
   document.getElementById(id).style.visibility = 'visible';
   ```

2. 按钮

   ```javascript
   <button type="button" onclick="document.getElementById('id1').style.color='red'">
   点击这里
   </button>
   ```

3. 事件反应

   我们可以对事件增添对应的JS代码从而实现我们对事件的反应

   **事件**

   * 点击鼠标

     * onmousedown:点击
     * onmouseup：释放
     * onclick:完成点击

   * 网页加载

     onload / onunload

     - onload：在用户进入页面触发
     - onunload：在用户离开页面触发

     可以用来处理cookie

     ```javascript
     <!DOCTYPE html>
     <html>
     <body onload="checkCookies()">

     <script>
     function checkCookies()
     {
     if (navigator.cookieEnabled==true)
     	{
     	alert("已启用 cookie")
     	}
     else
     	{
     	alert("未启用 cookie")
     	}
     }
     </script>

     <p>提示框会告诉你，浏览器是否已启用 cookie。</p>
     </body>
     </html>
     ```

   * 图像加载

   * 鼠标移动到元素上

     * onmouseover ： 鼠标覆盖到对应的元素上
     * onmouseout：鼠标离开对应的元素上

     ```javascript
     <div onmouseover="mOver(this)" onmouseout="mOut(this)" style="background-color:green;width:120px;height:20px;padding:40px;color:#ffffff;">把鼠标移到上面</div>
     <script>
     function mOver(obj)
     {
     obj.innerHTML="谢谢"
     }

     function mOut(obj)
     {
     obj.innerHTML="把鼠标移到上面"
     }
     </script>
     ```

   * 输入字段

     * onchange

       输入文本之后离开文本框会激活onchange事件

       ```javascript
       <input type="text" id="fname" onchange="upperCase()">
       ```

     * onfocus

       输入框获取焦点

       ```javascript
       <input type="text" id="fname" onchange="upperCase()">
       ```

   * 提交HTML表单

   * 触发按键

     ```javascript
     //1 点击该元素执行对应的onclick指令
     <h1 onclick="this.innerHTML='谢谢!'">请点击该文本</h1>
     //2 函数化，this的妙用
     <h1 onclick="changetext(this)">请点击该文本</h1>
     function changetext(id)
     {
     	id.innerHTML="谢谢!";
     }
     //3 分配事件,对onclick属性生成匿名函数
     <script>
     document.getElementById("myBtn").onclick=function(){displayDate()};
     </script>
     ```


## 3.DOM 节点

1. 创建

   * 创建元素

     ```javascript
     var para = document.createElement("p");    //创建p标签
     ```

   * 创建文本节点(节点概念参见上一个图)

     ```javascript
     var node = document.createTextNode("some text here\n");   //创建文本节点
     ```

   * 建立节点的父子关系

     ```javascript
     para.appendChild(node);    //文本节点是创建的新的p标签节点的子节点
     ```

2. 删除HTML元素

   **删除元素需要获得该元素的父元素**

   ```javascript
   parent.removeChild(child);    //parent是父节点，child是子节点，从父节点中移除子节点
   ```

   或者常用的解决方案

   ```javascript
   children.parentNode.removeChild(child);
   ```

# 三.JavaScript对象

## 1.JavaScript对象简介

1. 在JS中所有的事务都是对象，字符串，数组，数字，函数

2. JS存在內建对象

   * String
   * Date
   * Array

3. JS对象实际上是带有**属性**和**方法**的特殊数据类型

4. 访问属性

   ```javascript
   var message = "Hello World";
   var x = message.length;      //获取属性语法
   var x = message.toUpperCase();    //获取方法语法
   ```

5. JS允许自定义对象

   * 创建实例

     ```javascript
     //方法1
     var person = new Object();
     person.fname = 'lantian';
     person.lname = 'cao';
     //方法2
     person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};
     ```

   * 函数 - 对象构造器

     ```javascript
     function person(firstname,lastname,age,eyecolor)
     {
     this.firstname=firstname;
     this.lastname=lastname;
     this.age=age;
     this.eyecolor=eyecolor;
     }

     var per = new person("lantian" , 'GMFTBY' , 20 , 'blue');
     ```

   属性可以直接添加

   方法可以直接添加

   ```javascript
   function person(firstname,lastname,age,eyecolor)
   {
   	this.firstname=firstname;
   	this.lastname=lastname;
   	this.age=age;
   	this.eyecolor=eyecolor;
   	this.changeName=changeName;
   	function changeName(name)    //该函数也可以动态的外部添加但一般不常用
   	{
   		this.lastname=name;
   	}
   }
   ```

## 2.JavaScript 数字

1. 只存在一种数字类型

2. 支持科学计数法

3. 均为64位浮点数

4. 精度整数15位，小数最大位数是17位，浮点存在误差

5. 进制

   ```javascript
   var x = 03700;    //8
   var z = 0xFF;     //16
   ```

## 3.JavaScript字符串对象

1. replace

   ```javascript
   var str="Visit Microsoft!";
   document.write(str.replace(/Microsoft!/,"W3School"));
   ```

2. match

   ```javascript
   //match属性匹配到了返回对应的匹配字符串，否则返回null
   var str = "Hello World!";
   document.write(str.match("World") + "<br />");
   ```

3. indexOf

   ```javascript
   //返回匹配的字符串的首索引，否则返回-1
   document.write(str.indexOf("world"));
   ```

4. length

   ```javascript
   str.length    //属性
   ```

5. 样式

   http://www.w3school.com.cn/tiy/t.asp?f=jsrf_string_style

## 4.JavaScript日期对象

1. 创建

   ```javascript
   var mydate = new Date();    //默认使用当前时间作为默认值
   ```

2. 获取日期

   ```javascript
   mydate.getDate();    //获取天号
   mydate.getTime();    //从1970.1.1至今的毫秒数
   mydate.getDay();   //0 - 周日，1 - 周一,2 ...
   var h=today.getHours();
   var m=today.getMinutes();
   var s=today.getSeconds();
   t = setTimeout('function_name' , size);   //设定时间间隔循环启动函数执行
   ```

3. 操作日期

   ```javascript
   mydate.setFullYear(2008,7,9);    //月份在0 ~ 11
   mydate.setDate(mydate.getDate() + 5);    //增加天数5天,与分和年份的修改自动更正
   ```

4. 比较日期

   ```javascript
   > , < , >= , <= , !=     //均重载过
   ```

## 5.JavaScript数组对象

1. 定义数组

   ```javascript
   //1 任意多无限长数组
   var myarray = new Array();
   //2 控制容量数组
   var myarray = new Array(3);
   //3 初始化数组
   var myarray = new Array('lantian' , 'volvo' , 'gmftby');
   ```

2. 访问数组

   ```javascript
   document.write(myarray[0]);
   for(x in myarray)
     {
       //x是索引号
       //myarray[x]是对应的数据
     }
   ```

3. 修改

   ```javascript
   myarray[0] = 'GMFTBY';
   ```

4. 具体函数

   * `concat`

     ```javascript
     str.concat(str1);
     ```

   * `join`

     ```javascript
     str.join('.')    //连接数组成字符串，制定连接符号
     ```

   * `start`

     ```javascript
     str.sort(function_sort);     //改变原数组的排序
     function function_sort(a , b)
     {
       return a - b     //升序
       return b - a     //降序
     }
     ```

## 6.JavaScript逻辑对象

1. Boolean是一个产生逻辑值的对象包装器 ， 将其他的非逻辑对象转换成逻辑值 true / false

2. 创建

   ```javascript
   var myboolean = new Boolean();     //如果没有初始值或者初始值都是类零初始值默认都是false，否则是true
   ```

## 7.JavaScript算法对象

1. 执行常见的算数任务，提供多种的算数类型和函数，无需定义

2. 常见方法

   * 四舍五入

     ```javascript
     Math.round(4.7)    //5
     ```

   * 随机数

     ```javascript
     Math.random();    //随机数 0~1
     ```

   * floor向下取整

     ```javascript
     Math.floor(4.7);     //4
     ```

   * max / min

     ```javascript
     Math.max(1 , 2.0);
     Math.min(1 , 2.0);
     ```

3. 常见常数

   ```javascript
   Math.E    //e
   Math.PI    //3.1415926 ...
   Math.SQRT2   //sqrt(2)
   Math.SQRT1_2    //sqrt(0.5)
   Math.LN2    //ln2
   Math.LN10    //ln10
   Math.LOG2E    //log2 e
   Math.LOG10E    //log10 e
   ```

## 8.JavaScript正则表达式对象

1. 定义模式

   ```javascript
   var patt1=new RegExp("e" , 'g');    //g是检索模式，g代表全部检索，多次运行会不断的查找结果，这里使用while循环可以实现
   ```

2. 模式方法

   * test

     ```javascript
     document.write(patt1.test("The best things in life are free"));    //存在制定的模式返回true，否则返回false
     ```

   * exec

     ```javascript
     document.write(patt1.exec("The best things in life are free"));     //返回被模式匹配的对象，否则返回null
     ```

   * compile

     改变检索模式，或者删除添加检索模式

     ```javascript
     var patt1=new RegExp("e");
     document.write(patt1.test("The best things in life are free"));
     patt1.compile("d");   //修改检索的模式
     document.write(patt1.test("The best things in life are free"));
     ```

# 四.JavaScript Window

## 1.BOM 简介

1. 浏览器对象模型`BOM`

2. Window对象

   1. window表示浏览器窗口，所有的JS对象默认都是他的成员

   2. 全局变量是他的属性，全局函数是他的方法

   3. document根节点也是成员

      ```javascript
      window.document.getElementById("header");
      ```

## 2.JavaScript Location

1. 作用

   window.location 对象用于获得当前页面的地址 (URL)，并把浏览器重定向到新的页面。

2. 属性

   * location.hostname : 返回web主机域名
   * location.pathname / location.href: 前者返回当前页面的URL(相对主机的文件存放目录)，后者是绝对的URL地址
   * location.port : 返回web主机的端口
   * localtion.protocol : 返回使用的web协议

3. 方法

   * location.assign("URL") : 加载新的文档

## 3.JavaScript历史记录

1. window.history对象记录了浏览器的历史记录 ，可以不适用window前缀
2. 方法
   * history.back() : 后退前一个页面，加载历史中的前一个URL
   * history.forward() : 前进一个页面

## 4.JavaScript Navigator

1. window.navigator对象包含访问浏览器的信息 ， 可以放弃window前缀

2. navigator对象的信息会被使用者修改等等问题导致信息不可靠

3. 信息实例

   ```javascript
   <!DOCTYPE html>
   <html>
   <body>
   <div id="example"></div>
   <script>
   txt = "<p>Browser CodeName: " + navigator.appCodeName + "</p>";
   txt+= "<p>Browser Name: " + navigator.appName + "</p>";
   txt+= "<p>Browser Version: " + navigator.appVersion + "</p>";
   txt+= "<p>Cookies Enabled: " + navigator.cookieEnabled + "</p>";
   txt+= "<p>Platform: " + navigator.platform + "</p>";
   txt+= "<p>User-agent header: " + navigator.userAgent + "</p>";
   txt+= "<p>User-agent language: " + navigator.systemLanguage + "</p>";
   document.getElementById("example").innerHTML=txt;
   </script>
   </body>
   </html>
   ```

   结果

   ```
   Browser CodeName: Mozilla
   Browser Name: Netscape
   Browser Version: 5.0 (X11)
   Cookies Enabled: true
   Platform: Linux x86_64
   User-agent header: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
   User-agent language: undefined
   ```

## 5.JavaScript消息框

* alter

  ```javascript
  alter("text1" + "\n" + 'text2');    //在警示框中折行显示
  ```

* confirm ： 确认返回true否则返回false

  ```javascript
  <input type="button" onclick="show_confirm()" value="Show a confirm box" />
  function show_confirm()
  {
  var r=confirm("Press a button!");   //确认框
  if (r == true)
    {
    alert("You pressed OK!");
    }
  else
    {
    alert("You pressed Cancel!");
    }
  }
  ```

* prompt

  提示输入框，返回值是用户的输入值，否则是null

  ```javascript
  prompt("提示字符串" , "文本框默认文字")
  ```

## 6.JavaScript计时

1. 通过使用 JavaScript，我们有能力做到在一个设定的时间间隔之后来执行代码，而不是在函数被调用后立即执行。我们称之为计时事件。

2. 方法

   * setTimeout() : 

     1. 未来执行代码

     2. 参数

        setTimeout() 的第一个参数是含有 JavaScript 语句的字符串。这个语句可能诸如 "alert('5 seconds!')"，或者对函数的调用，诸如 alertMsg()"。

        第二个参数指示从当前起多少毫秒后执行第一个参数。

     3. 可以实现无穷循环，函数调用自身

   * clearTimeout() : 

     根据setTimeout返回的变量取消setTimeout代码

## 7.JavaScript Cookies

1. Cookie用来识别用户

2. cookie 是存储于访问者的计算机中的变量。每当同一台计算机通过浏览器请求某个页面时，就会发送这个 cookie。你可以使用 JavaScript 来创建和取回 cookie 的值。

3. cookie类型

   - 名字 cookie

     当访问者首次访问页面时，他或她也许会填写他/她们的名字。名字会存储于 cookie 中。当访问者再次访问网站时，他们会收到类似 "Welcome John Doe!" 的欢迎词。而名字则是从 cookie 中取回的。

   - 密码 cookie

     当访问者首次访问页面时，他或她也许会填写他/她们的密码。密码也可被存储于 cookie 中。当他们再次访问网站时，密码就会从 cookie 中取回。

   - 日期 cookie

     当访问者首次访问你的网站时，当前的日期可存储于 cookie 中。当他们再次访问网站时，他们会收到类似这样的一条消息："Your last visit was on Tuesday August 11, 2005!"。日期也是从 cookie 中取回的。

4. 创建和存储cookie

   1. 名字cookie

      ```javascript
      //value是名字，expires是过期时间,document.cookie对象
      document.cookie=c_name+ "=" +escape(value)+
      ((expiredays==null) ? "" : ";expires="+exdate.toGMTString())
      ```

# JavaScript 框架

矿建放在vue2.0中记录笔记，JS就这样

