# Vue2.0 JS框架

1. **`Vue.js`**是一套构建用户界面的小成本渐进增量的渐进式框架，专注于视图层，容易与其他的第三方库或者项目结合

2. 利用简介的模板将数据渲染成DOM(参见Javascript notebook.md)

3. 数据绑定 , 组件化

   页面上每一个组件，小到按钮都是一个单独的`.vue`文件,小组件可以更加灵活的组建起来

## 1.安装

* 项目建立

  vue-cli建立方法

  ```bash
  npm install vue    # 1
  npm install --global vue-cli    # 2
  vue init webpack my-project
  # 如果这一步失败，并且报错node文件找不到，是因为没有进入系统环境变量中，添加环境变量
  # ln -s /usr/bin/nodejs /usr/bin/node
  cd my-project
  npm install    # 加载依赖
  npm run dev    # localhost:8080中启动项目
  ```

* 简单测试的方法

  1. 网站https://vuejs.org/js/vue.min.js下载vue.js文本保存在本地
  2. 建立HTML在<script>中src引用这个本地的vue.js脚本就可以执行对用的vue脚本

## 2.目录结构

```bash
tree -L 1 .
.
├── README.md          项目使用命令说明
├── build              最终代码存放位置
├── config　　　        配置目录
├── index.html         首页入口文件
├── node_modules       npm加载的项目依赖模块
├── package.json       项目配置文件
├── src                项目开发目录，编写的代码在这里
│   ├── App.vue        项目的入口文件，可以直接将vue代码写在里面
│   ├── assets         图片等logo
│   ├── components     组件文件
│   ├── main.js        项目核心文件
│   └── router
├── static             静态资源目录，图片字体等
└── test               测试目录，可以删除
```

1. index.html调用执行对应的src文件中的vue组件
2. App.vue组件调用执行对于国内的组件目录下的相应的组件vue文件显示对应的元素

## 3.模板语法

1. 引入HTML5 <tempate>标签

   Vue.js 使用了基于 HTML 的模版语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。

   Vue.js 的核心是一个允许你采用简洁的模板语法来声明式的将数据渲染进 DOM 的系统。

   结合响应系统，在应用状态改变时， Vue 能够智能地计算出重新渲染组件的最小代价并应用到 DOM 操作上。

2. 文本生成

   1. `{{...}}`

      ```html
      <p>{{message}}</p><!--message绑定到对应的下面的Vue组件上-->
      <script>
      new Vue({
        el: '#app',
        data: {
          message: '<h1>菜鸟教程</h1>'
        }
      })
      </script>
      ```

   2. `v-html`

      使用v-html指令输出对应的HTML代码

      ```html
      <div id="app">
          <div v-html="message"></div>
      </div>    
      <script>
      new Vue({
        el: '#app',
        data: {
          message: '<h1>菜鸟教程</h1>'
        }
      })
      </script>
      ```

   属性绑定

   1. `v-bind`

      使用`v-bind`指令对我们的属性进行绑定

   2. `v-model`

      v-model这个指令只能用在`<input>`, `<select>`,`<textarea>`这些表单元素上，所谓双向绑定，指的就是我们在js中的vue实例中的data与其渲染的dom元素上的内容保持一致，两者无论谁被改变，另一方也会相应的更新为相同的数据。这是通过设置属性访问器实现的`

   ```html
   <style>
   .class1{
     background: #444;
     color: #eee;
   }
   </style>

   <div id="app">
     <label for="r1">修改颜色</label><input type="checkbox" v-model="class1" id="r1"><!--v-model实现双向绑定，将class1的属性绑定上去-->
     <br><br>
     <div v-bind:class="{'class1': class1}">
       directiva v-bind:class
     </div>
   </div>
   	
   <script>
   new Vue({
   	el: '#app',
     data:{
     	class1: false <!--将class1的属性隐藏，点击checkbox改为class1-->
     }
   });
   </script>
   ```

   表达式

   1. `vue.js`提供了对`JavaScript`的完整支持
   2. `data`中的数据将被导入到el所指向的对应的HTML元素中，在对应的HTML元素中可以使用对应的数据给JavaScript去执行

   ```html
   <div id="app">
       {{5+5}}<br>
       {{ ok ? 'YES' : 'NO' }}<br>
       {{ message.split('').reverse().join('') }}
       <div v-bind:id="'list-' + id">菜鸟教程</div>
   </div>
       
   <script>
   new Vue({
     el: '#app',
     data: {
       ok: true,
       message: 'RUNOOB',
       id : 1
     }
   })
   </script>
   ```

   ---

3. 指令

   1. 指令是带有`v-`前缀的特殊属性

   2. 指令可以将对应的改变反映在DOM上

   3. 示例 : v-if

      ```html
      <div id="app">
          <p v-if="seen">现在你看到我了</p>
          <template v-if = 'ok'>
            <h>Can you see me!</h>
          </template>
      </div>
          
      <script>
      new Vue({
        el: '#app',
        data: {
          seen: true
        }
      })
      </script>
      ```

   参数

   1. 参数是HTML元素后面制定的属性参数

   2. 指令的参数在　**`:`**　后指明

   3. `v-bind`指令被用来响应和绑定更新的HTML属性

      ```html
      <div id="app">
          <pre><a v-bind:href="url">菜鸟教程</a></pre><!--v-bind指令将元素的href属性和表达式url绑定-->
      </div>
          
      <script>
      new Vue({
        el: '#app',
        data: {
          url: 'http://www.runoob.com'
        }
      })
      </script>
      ```

   4. `v-on`指令可以监听DOM事件

      对于我们的DOM事件，我们的click属性可以用click之后的名称在`vue`的`data`中绑定

      ```html
      <a v-on:click='dosomething'>
      ```

   修饰符

   ​	修饰符是以半角句号 . 指明的特殊后缀，用于指出一个指定应该以特殊方式绑定。例如，.prevent 修	饰符告诉 v-on 指令对于触发的事件调用 event.preventDefault()：

   ```
   <form v-on:submit.prevent="onSubmit"></form>
   ```

   ---

4. 用户输入

   * 双向数据绑定

     `v-model`实现双向的数据绑定，DOM和vue.data中的元素属性是一致的

     `v-model`这个指令只能用在`<input>`, `<select>`,`<textarea>`这些表单元素上，所谓双向绑定，指的就是我们在js中的vue实例中的data与其渲染的dom元素上的内容保持一致，两者无论谁被改变，另一方也会相应的更新为相同的数据。这是通过设置属性访问器实现的

     ```html
     <div id="app">
         <p>{{ message }}</p>  <!--DOM上的属性显示-->
         <input v-model="message">  <!--绑定到对应的vue.data上，双向绑定，同时对input的修改也会自动的修改vue.data并显示在上面的{{message}}中-->
     </div>
         
     <script>
     new Vue({
       el: '#app',
       data: {
         message: 'Runoob!'
       }
     })
     </script>
     ```

   * 事件绑定

     ```html
     <div id="app">
         <p>{{ message }}</p>
         <button v-on:click="reverseMessage">反转字符串</button>
     </div>
         
     <script>
     //这里的this我们指定的是vue组件
     new Vue({
       el: '#app',
       data: {
         message: 'Runoob!'
       },
       methods: {
         reverseMessage: function () {
           this.message = this.message.split('').reverse().join('')
         }
       }
     })
     </script>
     ```

5. 过滤器

   1. 过滤器第一个参数是我们的后面的函数的参数
   2. 过滤器可以串联，类似于Linux下的管道
   3. 过滤器本质上是JS的函数，**用于对我们的用户的文本进行格式化处理**

   ```html
   <div id="app">
     {{ message | capitalize | next }}
   </div>
   	
   <script>
   new Vue({
     el: '#app',
     data: {
   	message: ''
     },
     filters: {
       capitalize: function (value) {
         if (!value) return 'fuck you guys'
         value = value.toString()
         return value.charAt(0).toUpperCase() + value.slice(1)　　//大写首字母
       },
       next: function (value) {
   	  return value + '\n' + 'nothing but GMFTBY';
       }
     }
   })
   </script>
   ```

6. vue实例

   1. 创建

      ```javascript
      var vm = new Vue({...})
      ```

   2. 属性与方法

      1. 每一个vue实例都会代理data对象里面的所有的属性(data对象)

         所谓的代理的意思就是data对象的属性就是vue的属性，可以实现双向的数据绑定

      2. `$`

         * `el` :

           el属性指代我们的DOM中的HTML文档元素，制定要绑定的元素

           ```javascript
           vm.$el === document.getElementById('example');   //el : '#example',结果是true
           ```

         * `data` 

           ```javascript
           var data = { a: 1 }
           var vm = new Vue({
             el: '#example',
             data: data
           })
           vm.$data === data // -> true
           ```

         * `watch`

           ```javascript
           vm.$watch('a', function (newVal, oldVal) {
             // 这个回调将在vm.a改变后调用
           })
           ```

## 4.条件and循环

### 条件

1. v-if / v-else / v-else-if

   ```html
   <div id="app">
       <div v-if="Math.random() > 0.5">
         Sorry
       </div>
       <div v-else-if="Math.random() < 0.3">
         Fuck
       </div>
       <div v-else>
         Not sorry
       </div>
   </div>
       
   <script>
   new Vue({
     el: '#app'
   })
   </script>
   ```

2. v-show

   ```html
   <h1 v-show='ok'>Hello!</h1>   <!--ok在vue.data中如果是true则显示，false则隐藏-->
   ```

### 循环

1. 循环使用`v-for`命令

2. 语法

   ```vue
   v-for='site in sites'    //sites是我们的data中的可迭代对象,site是我们设定的别名
   v-for='(value , key) in sites'    //可以使用python中类似的语法叫做序列解包，首先是值，后是值的索引
   v-for='(value , key , index) in sites'   //index是索引的数值
   v-for='site in 10'    //site可以在数字间迭代
   ```

   ```html
   <div id="app">
     <ol>
       <template v-for='site in sites'>
       	<li v-for="site in sites">
         		{{ site.name }}    <!--循环调用标签-->
       	</li>
       	<li>----------</li>
       </template>
     </ol>
   </div>

   <script>
   new Vue({
     el: '#app',
     data: {
       sites: [
         { name: 'Runoob' },
         { pname: 'Google' },
         { name: 'Taobao' }
       ]
     }
   })
   </script>
   ```

## 5.Vue计算属性

