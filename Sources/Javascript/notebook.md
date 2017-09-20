# JavaScript Notebook

## 1.什么是JavaScript

### 1.定义

1. JavaScript是轻量级的编程语言
2. JavaScript是可插入的HTML页面的编程代码
3. JavaScript插入HTML页面后，可以被现代的浏览器执行

### 2.简单使用

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

   1. 分好用来分割我们的JS语句
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

   ​