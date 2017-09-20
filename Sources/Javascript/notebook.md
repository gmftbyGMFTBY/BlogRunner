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

     ​

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
for(x in person)
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

