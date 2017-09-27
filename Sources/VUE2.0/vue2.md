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
├── build              最终代码存放位置，release之后的代码项目文件
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
2. App.vue组件调用执行对于components的组件目录下的相应的组件vue文件显示对应的元素

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
     <label for="r1">修改颜色</label>
     <input type="checkbox" v-model="class1" id="r1"><!--v-model实现双向绑定，将class1的属性绑定上去,这里的class1是和data的class1绑定，代表初始时checkbox的选值是false,之后可以根据选择替换我们的data.class1的值-->
     <br><br>
     <div v-bind:class="{'class1': class1}"><!--这里的键是字符串，值是data.class1-->
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
   3. `{{...}}`中允许我们执行表达式

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
          ok: false
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

     `v-model`这个指令只能用在`<input>`, `<select>`,`<textarea>`这些**表单元素**上，所谓双向绑定，指的就是我们在js中的vue实例中的data与其渲染的dom元素上的内容保持一致，两者无论谁被改变，另一方也会相应的更新为相同的数据。这是通过设置属性访问器实现的

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
       	<li>
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
         { name: 'Google' },
         { name: 'Taobao' }
       ]
     }
   })
   </script>
   ```

## 5.Vue计算属性

1. 什么是计算属性

   计算属性就是对我们的`vue.data`的属性在get之前进行计算，将计算结果返还，相当于是一个`getter`方法

   本质上其实`computed`和`methods`很类似，但是前者使用了缓存，性能更好一些

2. 实例

   ```html
   <div id="app">
     <p>原始字符串: {{ message }}</p>
     <p>计算后反转字符串: {{ reversedMessage }}</p>
   </div>
    
   <script>
   var vm = new Vue({
     el: '#app',
     data: {
       message: 'Runoob!'
     },
     computed: {
       // 计算属性的 getter
       reversedMessage: function () {
         // this 指向 vm 实例
         return this.message.split('').reverse().join('')
       }
     }
   })
   </script>
   ```

3. `getter` / `setter`

   ```html
   <script>
   var vm = new Vue({
     el: '#app',
     data: {
   	name: 'Google',
   	url: 'http://www.google.com'
     },
     computed: {
       site: {
         // getter
         get: function () {
           //this只带vue组件实例
           return this.name + ' ' + this.url
         },
         // setter
         set: function (newValue) {
           var names = newValue.split(' ')
           this.name = names[0]
           this.url = names[names.length - 1]
         }
       }
     }
   })
   // 调用 setter， vm.name 和 vm.url 也会被对应更新
   vm.site = '菜鸟教程 http://www.runoob.com';    //set方法
   document.write('name: ' + vm.name);     //get方法
   document.write('<br>');
   document.write('url: ' + vm.url);
   </script>
   ```


## 6.样式绑定

1. class / style　是我们对HTML属性进行设置的方式，**我们可以使用`v-bind`对样式进行绑定**

2. `v-bind`属性值可以是表达式，也可以是任意的对象

3. 实例(其实这个实例在上面已经出现过了)

   ```html
   <div v-bind:class="{'active': isActive }">
     <!--这里的active是上文中的一个.active类属性，isActive是下文中vue的一个data里额属性，在这里类属性的是否选择已经和变量绑定到一起了-->
   </div>
   <!--结果相当于是<div class="active"></div>-->
   ```

4. 更多实例

   ```html
   <style>
   .active {
   	width: 100px;
   	height: 100px;
   	background: green;
   }
   .text-danger {
   	background: red;
   }
   </style>
   </head>
   <body>
   <div id="app">
     <div class="static"
        v-bind:class="{ 'active': isActive, 'text-danger': hasError }">
     </div>
   </div>

   <script>
   new Vue({
     el: '#app',
     data: {
       isActive: true,
   	hasError: true
     }
   })
   //结果相当于是<div class="static active text-danger"></div>
   //css里面规定，如果多个样式修改的是同一个元素属性会后者覆盖前者，否则会叠加显示效果
   //还可以这样
   /*
   <div id="app">
     <div v-bind:class="classObject"></div>
   </div>

   <script>
   new Vue({
     el: '#app',
     data: {
       classObject: {
         active: true,
         'text-danger': true
       }
     }
   })

   //还可以注意的是，这里的classObject甚至还可以是我们的计算属性中的getter函数，只不过这个函数需要返回的是JS的对象，这个对象中的内容就是我们的data属性中的值

   //这里的v-bind:class后面设置还可以是数组，数组的元素是我们的dataJS对象中的键名,数组中甚至还可以使用三元运算符
   <div v-bind:class="[activeClass, errorClass]"></div>

   ------------------------------------------------------------
   <div id="app">
   	<div v-bind:class="[errorClass ,isActive ? activeClass : '']"></div>
   </div>
   <script>
   new Vue({
     el: '#app',
     data: {
       isActive: true,
   	activeClass: 'active',
       errorClass: 'text-danger'
     }
   })
   */
   </script>
   ```

5. vue内联样式

   v-bind:style可以直接制定我们的样式

   * 直接使用data中的对象构建对象型样式
   * 直接使用data的对象名
   * 直接使用数组，数组中引用相应的对象

   ```html
   <!--1，这个是值，直接构建JSON-->
   <div id="app">
       <div v-bind:style="{ color: activeColor, fontSize: fontSize + 'px' }">菜鸟教程</div>
   </div>
   <!--2，是一个JSON-->
   <div id="app">
     <div v-bind:style="styleObject">菜鸟教程</div>
   </div>
   <!--3,每个数组元素都是JSON-->
   <div id="app">
     <div v-bind:style="[baseStyles, overridingStyles]">菜鸟教程</div>
   </div>

   ```

## 7.事件处理器

1. `v-on:click`监听事件，我们的监听的事件可以是函数也可是对应的有关vue.data中的属性值的计算表达式

2. 如果`v-on`监听的是一个函数事件的话，没有传入参数的时候我们的传入的参数其实是触发这个函数的一个**事件对象**

   ```javascript
   //小的用法,event是我们的相应的事件对象
   event.target.TagName   //触发的HTML元素对象名称
   event.target    //触发的HTML元素对象本身,DOM
   ```

   传入参数的时候和我们的正常使用JS的语法一样

   ```javascript
   <button v-on:click="say">Say hi</button>  <!--传入事件对象-->
   <button v-on:click="say('what')">Say what</button>    <!--传入我们的参数-->
   ```

## 8.Vue表单

1. <input>表单元素和<textarea>表单元素

   我们使用`v-model`可以将表单中的数据和我们的vue.data中的数据实现双向绑定

2. `checkbox`的使用

   表单元素存在有value属性，如果我们的绑定的vue.data的值和这个value属性的值相同，则选中否则不选中(选中在复选框中可以在数组中叠加，单选框中我们的vue.data的值和那个表单的value属性相同初始默认就是选中那个表单元素)

   **简而言之我们双向绑定的数据，是vue.data和表单元素的value属性的双向绑定，如果value属性不存在默认是false(Boolean),单选是个特例，这里我们的但须默认的是true和false的属性进行切换**

   * `v-model`可以将我们的vue.data中的boolean值绑定到对应的checkbox的表单上，并且是双向

     绑定

   * 如果checkbox中存在value属性并且绑定的是我们的数组类型的对象，可以实现复选框的信息的收集

   * <select>

     ```html
     <select>
       <option value="">default</option>
       <option value="ddddd"></option>
     </select>
     ```

   ```html
   <div id="app">
     <p>单个复选框：</p>
     <input type="checkbox" id="checkbox" v-model="checked">
     <label for="checkbox">{{ checked }}</label>
       
     <p>多个复选框：</p>
     <input type="checkbox" id="runoob" value="Runoob" v-model="checkedNames">
     <label for="runoob">Runoob</label>
     <input type="checkbox" id="google" value="Google" v-model="checkedNames">
     <label for="google">Google</label>
     <input type="checkbox" id="taobao" value="Taobao" v-model="checkedNames">
     <label for="taobao">taobao</label>
     <br>
     <span>选择的值为: {{ checkedNames }}</span>
   </div>
    
   <script>
   new Vue({
     el: '#app',
     data: {
       checked : false,
       checkedNames: []
     }
   })
   </script>
   ```

3. 修饰符

   有用的修饰符使用

   * ```html
     <input v-model.number="..." type="number">   //将输入的数据自动从字符串转成数字
     ```

   * ```html
     <input v-model.trim="msg">   //过滤用户输入的首尾空格
     ```

## 9.Vue组件

### 简要介绍

1. vue组件是最强大的vue功能
2. 扩展HTML元素，封装可重用代码(将HTML元素动态的绑定到vue元素上实现一些html元素的扩展变化)
3. 组件可以构建一个大的应用，**形成一个组件树**

### 使用方法

* 全局组件

  ```html
  <script>
  // 注册
  Vue.component('runoob', {
    template: '<h1>自定义组件!</h1>'
  })
  // 创建根实例
  new Vue({
    el: '#app'
  })
  </script>

  <div id="app">
      <runoob></runoob>
  </div>
  ```

* 局部组件

  ```html
  <div id="app">
      <runoob></runoob>
  </div>
   
  <script>
  var Child = {
    template: '<h1>自定义组件!</h1>'
  }
   
  // 创建根实例
  new Vue({
    el: '#app',
    components: {
      // <runoob> 将只在父模板可用
      'runoob': Child
    }
  })
  </script>s
  ```

* prop

  ```html
  <div id="app">
      <div>
        <input v-model="parentMsg">
        <br>
        <child v-bind:message="parentMsg"></child>
      </div>
  </div>
   
  <script>
  // 注册
  Vue.component('child', {
    // 声明 props
    props: ['message'],
    // 同样也可以在 vm 实例中像 "this.message" 这样使用
    template: '<span>{{ message }}</span>'
  })
  // 创建根实例
  new Vue({
    el: '#app',
    data: {
      parentMsg: '父组件内容'
    }
  })
  </script>
  ```

## 10.Vue自定义指令

1. 除了`v-model`,`v-on`,vue允许我们制定自定义的指令

2. 相关函数和参数

   * 参数

     * el : 指令绑定的HTML元素,可以用来改变DOM

   * 函数

     * inserted : 指令的绑定的函数在绑定的元素被插入父节点的时候调用

       ```html
       <!-- 全局 -->
       <script>
       // 注册一个全局自定义指令 v-focus
       Vue.directive('focus', {
         // 当绑定元素插入到 DOM 中。
         inserted: function (el) {
           // 聚焦元素
           el.focus()
         }
       })
       // 创建根实例
       new Vue({
         el: '#app'
       })
       </script>
       <!-- 局部 -->
       <script>
       // 创建根实例
       new Vue({
         el: '#app',
         directives: {
           // 注册一个局部的自定义指令 v-focus
           focus: {
             // 指令的定义
             inserted: function (el) {
               // 聚焦元素
               el.focus()
             }
           }
         }
       })
       </script>
       ```

     * bind : 指令第一次绑定在元素上的额时候调用，一般执行初始化操作

     * unbind : 解绑时调用

   * 省略制定的函数

     ```html
     <script>
     Vue.directive('runoob', function (el, binding) {
         // 简写方式设置文本及背景颜色
         el.innerHTML = binding.value.text
         el.style.backgroundColor = binding.value.color
     })
     new Vue({
       el: '#app'
     })
     </script>
     <div id="app">
         <div v-runoob="{ color: 'green', text: '菜鸟教程!' }"></div>
     </div>
     ```

## 11.Vue路由

1. Vue.js 路由允许我们通过不同的 URL 访问不同的内容。

2. vue.js + vue.router.js可以实现简单的**单页应用**

3. 需要外部导入库

   * 直接使用

     ```bash
     wget https://unpkg.com/vue-router/dist/vue-router.js
     ```

   * 工程内使用

     ```bash
     npm install vue-router
     ```

4. 使用

   HTML:

   ```html
   <div id="app">
     <h1>Hello App!</h1>
     <p>
       <!-- 使用 router-link 组件来导航. -->
       <!-- 通过传入 `to` 属性指定链接. -->
       <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->
       <router-link to="/foo">Go to Foo</router-link>
       <router-link to="/bar">Go to Bar</router-link>
     </p>
     <!-- 路由出口 -->
     <!-- 路由匹配到的组件将渲染在这里 -->
     <router-view></router-view>
   </div>
   ```

   JS:

   ```HTML
   <script>
   // 0. 如果使用模块化机制编程，導入Vue和VueRouter，要调用 Vue.use(VueRouter)
   // 1. 定义（路由）组件。
   // 可以从其他文件 import 进来
   // 这决定如何去渲染
   const Foo = { template: '<div>foo</div>' }
   const Bar = { template: '<div>bar</div>' }

   // 2. 定义路由
   // 每个路由应该映射一个组件。 其中"component" 还可以是
   // 通过 Vue.extend() 创建的组件构造器，
   // 或者，只是一个组件配置对象。
   const routes = [
     { path: '/foo', component: Foo },
     { path: '/bar', component: Bar }
   ]

   // 3. 创建 router 实例，然后传 `routes` 配置
   // 你还可以传别的配置参数, 不过先这么简单着吧。
   const router = new VueRouter({
     routes:routes
   })

   // 4. 创建和挂载根实例。
   // 记得要通过 router 配置参数注入路由，
   // 从而让整个应用都有路由功能
   const app = new Vue({
     router,
     el: '#app'
   })
   </script>
   ```

   ​