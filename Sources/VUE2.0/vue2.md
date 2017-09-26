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

