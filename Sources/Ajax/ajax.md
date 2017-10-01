# AJAX

## Begin

1. 异步JavaScript和XML的新的方法

2. **是一种在不加载整个网页的情况下**和服务器交换数据并更新部分网页的技术

   通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新，**然而传统的网页需要重新加载页面才能更新内容**

3. 创建快速动态网页的技术

   例如 : 

   百度或者谷歌的搜索引擎在搜索框中输入要查询的数据的时候，会自动的从服务器中返回一个搜索建议的列表

4. 再次强调AJAX并不是一种编程语言，它只是一种利用`JS , HTML , CSS`实现的异步加载网页的方法技术

## AJAX XMLHttpRequest

1. XMLHttpRequest是AJAX的基础

2. 所有现代浏览器均支持 XMLHttpRequest 对象（IE5 和 IE6 使用 ActiveXObject）。

   XMLHttpRequest 用于在后台与服务器交换数据。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

3. 创建XHR对象

   ```javascript
   // 检查是否需可以使用XHR
   if(window.XMLHttpRequest == true){ ... }
   // 创建
   var v = new XMLHttpRequest();
   ```

4. XHR发送服务器请求

   * 方法

     * open(method , url , async) 

       e.g.

       ```javascript
       xmlhttp.open('GET' , 'test1.txt' , true)
       ```

       规定请求的类型以及制定的URL和是否允许进行异步处理

       * method : 'GET' / 'POST'
       * URL : 文件在服务器上的位置
       * async : true 异步 false 同步，想要使用AJAX技术该值必须是true

     * send(string)

       将open的请求发送到指定的服务器，只是针对'POST'请求的

   * GET V.S. POST

     1. get请求的速度快，大部分情况先都可以使用
     2. 必须使用post
        * 无法缓存文件(跟新服务器的数据)
        * 大量数据发送(post没有限制数据的发送的大小)
        * 安全性高

   * 其他

     * 有时候我们的AJAX给我们提供的是我们的缓存的数据，并不是真正在服务器山请求的数据，这时候我们可以给我们的请求的文件的名加上一个为一个的信息作为标识可以解决这种情况

       ```javascript
       xmlhttp.open("GET","demo_get.asp?t=" + Math.random(),true);
       xmlhttp.send();
       ```

     * get请求发送信息的时候

       ```javascript
       // 将要提交的数据含在get请求中，相当于一个post请求
       xmlhttp.open("GET","demo_get2.asp?fname=Bill&lname=Gates",true);
       xmlhttp.send();
       ```

     * 如果需要post HTML表单的数据

       如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据

       ```javascript
       xmlhttp.open("POST","ajax_test.asp",true);
       xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
       xmlhttp.send("fname=Bill&lname=Gates");
       ```

       setRequestHeader(*header*,*value*)

       * 头名称
       * 规定头的值

     * `onreadystatechange`

       当async是true(AJAX启动时)

       在该函数中可以定义我们在异步加载的时候需要调用的函数

       ```javascript
       xmlhttp.onreadystatechange=function()
         {
         if (xmlhttp.readyState==4 && xmlhttp.status==200)
           {
           document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
           }
         }
       xmlhttp.open("GET","test1.txt",true);
       xmlhttp.send();
       ```

     * 所谓的"异步"

       JS在我们的服务器的请求还没有发送到客户端的时候执行其他的脚本，当我们的服务器的相应到达的时候会执行服务器的响应结果，如果是同步的话，我们的JS会无限期等待服务器的响应二暂停进程

5. XHR 服务器响应

   * 属性

     * responseText : 字符串的形式获得响应数据

       在`onreadystatechange`函数中可以

       ```javascript
       document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
       ```

     * responseXML : XML的形式获取响应的数据

       ```javascript
       xmlhttp.onreadystatechange=function()
         {
         if (xmlhttp.readyState==4 && xmlhttp.status==200)
           {
           xmlDoc=xmlhttp.responseXML;
           txt="";
             //　下面是XML的语法
           x=xmlDoc.getElementsByTagName("title");
           for (i=0;i<x.length;i++)
             {
             txt=txt + x[i].childNodes[0].nodeValue + "<br />";
             }
           document.getElementById("myDiv").innerHTML=txt;
           }
         }
       xmlhttp.open("GET","/example/xmle/books.xml",true);
       xmlhttp.send();
       }
       ```

6. XHR onreadystatechange事件

   1. 当请求被发送到服务器时，我们需要执行一些基于响应的任务。

   2. 每当 readyState 改变时，就会触发 onreadystatechange 事件。

      readyState是XHR的内置属性，readyState 属性存有 XMLHttpRequest 的状态信息。

   3. 其他的重要属性

      * onreadystatechange :

        1. 存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数
        2. onreadystatechange 事件被触发 5 次（0 - 4），对应着 readyState 的每个变化

      * readyState : 

        存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。

        - 0: 请求未初始化
        - 1: 服务器连接已建立
        - 2: 请求已接收
        - 3: 请求处理中
        - 4: 请求已完成，且响应已就绪

      * status : 

        常用的请求状态

        * 200 - OK
        * 404 - 未找到页面

      我们经常使用为了保证安全的语句

      ```javascript
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
      ```

   4. callback函数

      1. 是一种将一个函数作为参数床底给另一个函数的方式
      2. 如果您的网站上存在多个 AJAX 任务，那么您应该为创建 XMLHttpRequest 对象编写一个*标准*的函数，并为每个 AJAX 任务调用该函数。
      3. 该函数调用应该包含 URL 以及发生 onreadystatechange 事件时执行的任务(最好是匿名的函数)（每次调用可能不尽相同）

      ```html
      <html>
      <head>
      <script type="text/javascript">
      var xmlhttp;
      function loadXMLDoc(url,cfunc)
      {
      if (window.XMLHttpRequest)
        {// code for IE7+, Firefox, Chrome, Opera, Safari
        xmlhttp=new XMLHttpRequest();
        }
      else
        {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
      xmlhttp.onreadystatechange=cfunc;
      xmlhttp.open("GET",url,true);
      xmlhttp.send();
      }
      function myFunction()
      {
      loadXMLDoc("/ajax/test1.txt",function()
        {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
          {
          document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
          }
        });
      }
      </script>
      </head>
      <body>

      <div id="myDiv"><h2>Let AJAX change this text</h2></div>
      <button type="button" onclick="myFunction()">通过 AJAX 改变内容</button>

      </body>
      </html>
      ```

## Harder

1. **AJAX 用于创造动态性更强的应用程序**

2. AJAX和asp / php

   ```html
   <html>
   <head>
   <script type="text/javascript">
   function showHint(str)
   {
   var xmlhttp;
   if (str.length==0)
     { 
     document.getElementById("txtHint").innerHTML="";
     return;
     }
   if (window.XMLHttpRequest)
     {// code for IE7+, Firefox, Chrome, Opera, Safari
     xmlhttp=new XMLHttpRequest();
     }
   else
     {// code for IE6, IE5
     xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
     }
   xmlhttp.onreadystatechange=function()
     {
     if (xmlhttp.readyState==4 && xmlhttp.status==200)
       {
       document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
       }
     }
   xmlhttp.open("GET","/ajax/gethint.asp?q="+str,true);
   xmlhttp.send();
   }
   </script>
   </head>
   <body>

   <h3>请在下面的输入框中键入字母（A - Z）：</h3>
   <form action=""> 
   姓氏：<input type="text" id="txt1" onkeyup="showHint(this.value)" />
   </form>
   <!-- onkeyup函数指代的意思是我们在输入的同时会执行该函数 -->
   <p>建议：<span id="txtHint"></span></p> 

   </body>
   </html>
   ```

3. AJAX和数据库

   对数据库的访问是需要我们的asp / php语言的执行实现的，当然也可以是Python