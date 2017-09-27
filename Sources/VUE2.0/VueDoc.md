# Vue Document Study

## 介绍

1. Vue的核心在于帮助你使用简介的模板语法来声明式的将数据渲染进DOM

2. 组件化应用构建

   1. 组件系统是 Vue 的另一个重要概念，因为它是一种抽象，允许我们使用小型、独立和通常可复用的组件构建大型应用。仔细想想，几乎任意类型的应用界面都可以抽象为一个组件树

   2. 组件的定义 : 拥有预定义选项的Vue实例

   3. 注册组件

      ```javascript
      Vue.component('todo-item', {
        template: '<li>这是个待办项</li>'
      })
      ```

      定义的组件是固定的，也就是说我们仅仅是实现了一个新的标签而已，我们需要对我们的标签传递参数使其多样化

      ```javascript
      //vue组件的全局声明
      Vue.component('todo-item', {
        // todo-item 组件现在接受一个
        // "prop"，类似于一个自定义属性
        // 这个属性名为 todo。
        props: ['todo'],
        template: '<li>{{ todo.text }}</li>'
      })
      //创建组件的实例
      var app7 = new Vue({
        el: '#app-7',
        data: {
          groceryList: [
            { id: 0, text: '蔬菜' },
            { id: 1, text: '奶酪' },
            { id: 2, text: '随便其他什么人吃的东西' }
          ]
        }
      })
      //HTML
      <div id="app-7">
        <ol>
          <!--
            现在我们为每个 todo-item 提供 todo 对象
            todo 对象是变量，即其内容可以是动态的。
            我们也需要为每个组件提供一个“key”，晚些时候我们会做个解释。
          -->
          <todo-item
            v-for="item in groceryList"
            v-bind:todo="item"
            v-bind:key="item.id">
          </todo-item>
        </ol>
      </div>
      //在整个流程中，app7实例是父单元，提供必要的数据，子单元是我们的<todo-item>，`v-bind:todo`绑定的属性调用我们的`template`模板输出对应的父单元传递的数据
      ```

      结果分析:

      1. 在这里，我们的子单元成功的实现了父单元的参数的传递和接收
      2. 实现了子单元和父单元的分离，两者只需要传递具体的参数就可以，可以对两个单元分别设计更复杂的逻辑

## Vue实例

1. 每一个Vue都是通过创建对应的Vue实例开始的

   ```javascript
   var vm = new Vue({//选项参数...})
   ```

2. 我们需要注意的所有焦点就是如何设计我们的选项参数构建符合要求的Vue组件

3. 一个 Vue 应用由一个通过 `new Vue` 创建的**根 Vue 实例**，以及可选的嵌套的、可复用的组件树组成

4. 数据和方法

   * 只有Vue.data中的数据是响应式的，其他并不是相应式的，当Vue.data中的数据改变的时候，视图会重新进行渲染

   * 除了 data 属性，Vue 实例暴露了一些有用的实例属性与方法。它们都有前缀 `$`，以便与用户定义的属性区分开来

     ```javascript
     var data = { a: 1 }
     var vm = new Vue({
       el: '#example',
       data: data
     })
     vm.$data === data // => true
     vm.$el === document.getElementById('example') // => true
     // $watch 是一个实例方法
     vm.$watch('a', function (newValue, oldValue) {
       // 这个回调将在 `vm.a` 改变后调用
     })
     ```

5. 实例的生命周期

   1. 每个 Vue 实例在被创建之前都要经过一系列的初始化过程。例如需要设置数据监听、编译模板、挂载实例到 DOM、在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做**生命周期钩子**的函数，给予用户机会在一些特定的场景下(特定的生命周期下)添加他们自己的代码。

      钩子函数的this指向我们的vue实例

      * created:

        比如 [`created`](https://cn.vuejs.org/v2/api/#created) 钩子可以用来在一个实例被创建之后执行代码：

        ```javascript
        new Vue({
          data: {
            a: 1
          },
          created: function () {
            // `this` 指向 vm 实例
            console.log('a is: ' + this.a)
          }
        })
        // => "a is: 1"
        ```

      * mounted

      * updated

      * destroyed

   2. 图示

      ![Vue 实例生命周期](https://cn.vuejs.org/images/lifecycle.png)

## 模板语法

1. Vue.js 使用了基于 HTML 的模板语法，允许开发者声明式地将 DOM 绑定至底层 Vue 实例的数据。所有 Vue.js 的模板都是合法的 HTML ，所以能被遵循规范的浏览器和 HTML 解析器解析。
2. 文本
   * {{...}}是动态绑定的，可以使用`v-once`指令断绝这种动态绑定
3. 属性 / 参数

   1. 不能在 Vue 模板中的 HTML 属性上使用双花括号语法(mustache)，而应该使用 
   2. v-bind 指令也同样适用于布尔类的属性 - 如果条件取值后是一个 false 值，属性将会从 DOM 中移除
   3. 一些指令能够接收一个“参数”，在指令名称之后以 `:` 表示
4. JS支持

   1. Vue实现了我们对JS的部分语句支持，首先我们对JS只支持表达式不支持语句和流控制,循环语句
   2. 模板表达式放置在沙盒中，只能访问全局变量的一个白名单列表，如 `Math` 和 `Date`。在模板表达式中，你不应该试图访问用户定义的全局变量。
5. 指令显示

   1. 指令(directive)是带有 `v-` 前缀的特殊属性。指令属性的值期望接收的是**单个 JavaScript 表达式**（`v-for` 是例外情况，稍后我们再讨论）。指令的职责是，当表达式的值改变时，将其产生的影响效果，响应式地作用于 DOM

## computed && watcher

* computed属性（一种属是通过函数生成的动态属性）

  1. 定义getter / settter方法

  2. method同样可以实现相同的逻辑，**computed 属性会基于它所依赖的数据进行缓存**

     这样也就意味着如果我们的computed会将我们的之前计算的结果保存起来当做缓存，如果我们的原先的computed没有改变的话，我们是不会重新进行渲染的，性能会好一点相比之下,method总是重新执行程序

  3. computed 属性默认只设置 getter 函数，不过在需要时，还可以提供 setter 函数

     ```javascript
     // ...
     computed: {
       fullName: {
         // getter 函数
         get: function () {
           return this.firstName + ' ' + this.lastName
         },
         // setter 函数
         set: function (newValue) {
           var names = newValue.split(' ')
           this.firstName = names[0]
           this.lastName = names[names.length - 1]
         }
       }
     }
     // ..
     ```

* watch属性

  1. Vue 其实还提供了一种更加通用的方式，来观察和响应 Vue 实例上的数据变化：**watch 属性**
  2. 建议不要使用watch函数来进行数据的动态绑定

## class && style

### Class

1. `v-bind`可以实现我们的class , style属性的绑定

2. 我们可以向 `v-bind:class` 传入一个对象，来动态地切换 class

   ```javascript
   <div v-bind:class="{ active: isActive }"></div>
   ```

3. 这样，可以通过在对象中添加多个字段，来切换多个 class。此外，`v-bind:class` 指令也可以和普通 `class` 属性共存

   ```javascript
   <div class="static"
        v-bind:class="{ active: isActive, 'text-danger': hasError }">
   </div>
   data: {
     isActive: true,
     hasError: false
   }
   ```

   属性还可以绑定到对应的JS对象(我们可以利用computed返回一个JS对象)上，JS对象保存在data中才可以被识别

4. class中的父子关系

   父

   ```javascript
   Vue.component('my-component', {
     template: '<p class="foo bar">Hi</p>'
   })
   ```

   子

   ```javascript
   <my-component class="baz boo"></my-component>
   ```

   上面最后的子的class是 : foo bar baz boo，**父的class是不会被覆盖的只会被继承**

### Style

1. 好的做法

   ```javascript
   <div v-bind:style="styleObject"></div>
   -------
   data: {
     styleObject: {
       color: 'red',
       fontSize: '13px'
     }
   }
   同样的，还可以绑定到对应的JS对象(我们可以利用computed返回一个JS对象)上，JS对象保存在data中才可以被识别
   ```

## 条件渲染

条件渲染支持JS表达式

1. <template>中使用`if-ok`

   ```javascript
   <template v-if="ok">
     <h1>Title</h1>
     <p>Paragraph 1</p>
     <p>Paragraph 2</p>
   </template>
   ```

2. 控制Vue的渲染

   1. 首先我们需要知道，Vue本身使用了很高效的机制来对我们的一些元素做渲染，Vue 尝试尽可能高效的渲染元素，通常会**复用**已有元素而不是从头开始渲染

      e.g.

      ```javascript
      <template v-if="loginType === 'username'">
        <label>Username</label>
        <input placeholder="Enter your username">
      </template>
      <template v-else>
        <label>Email</label>
        <input placeholder="Enter your email address">
      </template>
      <!-- 这里的两个input在if-else中被复用了，所以我们上一次在文本框中的输入就会在下一次显示出来 -->
      ```

   2. 解决方案就是对HTML元素使用key属性，key属性值必须唯一，保证Vue不会复用我们的HTML元素

## 循环列表渲染

使用`v-for`循环遍历我们的**数组或者对象**，将我们的数组渲染成列表

对于我们的对象来说，我们的生成的顺序是不一致是随机的

```javascript
<ul id="example-1">
  <li v-for="(item , key , index ) in items">
    {{ item.message }}
  </li>
</ul>

var example1 = new Vue({
  el: '#example-1',
  data: {
    items: [
      { message: 'Foo' },
      { message: 'Bar' }
    ]
  }
})
```

对于数组的变化更新，Vue 将观察数组(observed array)的变化数组方法(mutation method)包裹起来，以便在调用这些方法时，也能够触发视图更新。这些包裹的方法如下

* push()
* pop()
* shift()
* unshift()
* splice()
* sort()
* reverse()

变化的数组之后会自动的的反映在视图上

如果数组没有变化，但是我们返回数组的其中一部分的时候也会触发视图的更新

* filter()
* concat()
* slice()
* match()

Vue 不允许在已经创建的实例上，动态地添加新的根级响应式属性

## 事件处理器

1. 监听事件

   `v-on:click`可以绑定函数也可以绑定JS表达式(或者JS格式函数调用)

## 组件

组件(component)是 Vue 最强大的功能之一。组件可以帮助你扩展基本的 HTML 元素，以封装可重用代码。在较高层面上，组件是 Vue 编译器附加行为后的自定义元素。在某些情况下，组件也可以是原生 HTML 元素的形式，以特定的 `is` 特性扩展。

1. 全局组件

   要注册一个全局组件，你可以使用 `Vue.component(tagName, options)`

2. 局部组件

   没有必要将每个组件都注册在全局。你可以通过实例的 `components` 选项，将组件注册在局部，可以使组件只能从其他实例/组件的作用域范围中访问到

3. 错误

   1. 在这些受限制的元素中使用自定义元素，会导致一些问题

   2. 自定义组件 `<my-row>` 将会被当作无效内容，解决方案是使用特殊的 `is` 属性

      ```javascript
      <table>
        <tr is="my-row"></tr>
      </table>
      ```

      ​