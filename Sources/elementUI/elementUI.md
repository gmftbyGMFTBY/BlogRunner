# ElementUI Document

## 安装

```
# 在vue.js或者其他的JS框架中安装
npm i element-ui -S
# 安装到node_modules依赖文件夹中
# 在安装elementUI官方示例的时候，我们可能会月到一个很严重的问题就是NodeJS和npm之间版本低的问题
# 在升级npm中显示NodeJS和npm版本不符合的时候，优先升级node版本，目前的最新版本在官网[http://nodejs.org/en/]下载之后在本地解压，将node可执行文件cp到/usr/bin中即可
# npm install -g npm 之后升级npm目前最高本本是5.4
# 在官方示例的工程中我们执行 npm install下载node_moduels依赖包
# npm run dev 打开工程
```

## 快速入门

1. 项目结构

   ```bash
   tree .
   ├── Makefile
   ├── README.md               # 项目帮助文档
   ├── package.json            # npm配置文件
   ├── postcss.config.js
   |── .babelrc                # babel配置文件
   ├── src                     # 项目源代码
   │   ├── App.vue
   │   ├── assets
   │   │   └── logo.png
   │   ├── index.html          # HTML模板
   │   ├── main.js             # 入口文件 
   │   └── vendor.js
   ├── webpack.config.js       # webpack配置文件
   └── yarn.lock
   ```

2. 引入Element

   你可以引入整个 Element，或是根据需要仅引入部分组件。

   * 完整引入

     ```javascript
     // main.js中或者其他的项目文件
     //　需要保证项目中的node_models目录下存在对应的element-ui的依赖目录
     import ElementUI from 'element-ui'
     import 'element-ui/lib/theme-default/index.css'    //样式的CSS文件需要单独引入

     Vue.use(ElementUI)     // Vue组件全局使用Element-UI
     ```

   * 按需求引入

     借助 [babel-plugin-component](https://github.com/QingWei-Li/babel-plugin-component)，我们可以只引入需要的组件，以达到减小项目体积的目的。

     * 安装

       ```bash
       # 项目目录下
       npm install babel-plugin-component -D
       ```

     * 使用详情参见官方文档

3. 使用

   现在基于Vue + Element的开发环境搭建完毕

   ```bash
   # 启动
   npm run dev
   # 编译
   npm run build
   ```

## 语言

Element内部的组件默认使用中文，可以导入别的语言文字

```javascript
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'

Vue.use(ElementUI, { locale })
```

## 自定义主题

1. 安装主题生成工具

   ```bash
   npm i element-theme -g    # 全局安装或者在项目下安装都可以
   # 最新
   npm i element-theme-default -D
   ```

2. 初始化变量文件

   主题生成工具安装成功后，如果全局安装可以在命令行里通过 `et` 调用工具，如果安装在当前目录下，需要通过 `node_modules/.bin/et` 访问到命令。执行 `-i` 初始化变量文件。默认输出到 `element-variables.css`，当然你可以传参数指定文件输出目录

   ```bash
   et -i [自定义变量文件]
   ```

3. 修改变量文件

   直接打开我们的`element-variables.css`文件或者我们的输出文件修改CSS样式

4. 编译主题

   修改完我们的变量文件之后，我们可以在`et`中编译我们的主题文件

   ```bash
   # w : 监视模式，实时预览我们的编译过程
   # c : 制定编译的变量文件
   et -c file_name -w
   ```

5. 导入自定义主题

   默认的主题保存在../theme文件夹下，在import中可以指定导入路径