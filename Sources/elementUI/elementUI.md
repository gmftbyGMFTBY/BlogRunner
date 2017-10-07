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

## 基本组件

### 基础

#### Layout

使用基础的24分栏布局

1. <el-row> :行布局，使用的行标签 

   * gitter属性支持在列级分栏中插入间隔,默认间隔是0

     ```html
     <el-row :gutter='20'></el-row>
     ```

   * type属性赋值成`flex`可以启动flex布局，在flex布局中可以使用justify属性对我们的row中的列元素**整体**进行特定的布局分布排列

     justify : 水平排列

     * start : 左对齐
     * end : 右对齐
     * center : 居中
     * space-between : 均分间隔，左右两边贴边界
     * space-around : 均分间隔，左右两边不贴边界

     align : 竖直排列

     * top
     * middle
     * bottomsur

     ```html
     <el-row type='flex' justify="start"></el-row>
     <el-row type='flex' justify="end"></el-row>
     <el-row type='flex' justify="center"></el-row>
     <el-row type='flex' justify="space-between"></el-row>
     <el-row type='flex' justify="space-around"></el-row>
     ```

2. <el-col>:列布局，

   * 支持使用span标签进行行内的分栏(24分,24,12,8,6,4,3,2,1)

     ```html
     <el-col :span = '24'></el-col>
     <el-col :span = '12'></el-col>
     <el-col :span = '6'></el-col>
     <el-col :span = '3'></el-col>
     <el-col :span = '8'></el-col>
     <el-col :span = '2'></el-col>
     <el-col :span = '4'></el-col>
     <el-col :span = '1'></el-col>
     ```

   * offset属性支持进行偏移,使用24分栏定义偏移的栏数

     ```html
     <el-col :span='6' :offset="6"></el-col>
     ```

   * xs : < 768px像素的超小屏手机显示的时候的span

   * sm : > 768px像素的平板显示span

   * md : > 992px台式电脑

   * lg : > 1200超大电脑显示的span

#### Color

http://element.eleme.io/#/zh-CN/component/color查看更多的色彩配方

#### Typography

```css
font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
```

#### Icon && Button

1. <i>

   * <i>标签可以应用已经定义的图标我们使用，名称一般是`el-icon-iconName`
   * 更多的图标样式参照官网http://element.eleme.io/#/zh-CN/component/icon

   ```html
   <i class="el-icon-edit"></i>
   <i class="el-icon-share"></i>
   <i class="el-icon-delete"></i>
   <el-button type="primary" icon="search">搜索</el-button>    <!-- 我们的button中也可以嵌入icon显示，更美观 -->
   ```

2. <el-button>

   1. 在element中我们可以对button进行7中不同的定义

      使用type属性

      - 默认
      - primary : 主要按钮
      - text : 文字按钮
      - success : 操作成功按钮
      - warning : 操作警告按钮
      - danger : 危险操作按钮
      - info : 信息按钮

      ```html
      <el-button>默认按钮</el-button>
      <el-button type="primary">主要按钮</el-button>
      <el-button type="text">文字按钮</el-button>
      ```

   2. 禁用按钮

      ```html
      <el-button type="primary" icon="search" :disabled='true'>搜索</el-button>
      ```

   3. plain参数，忽视颜色，颜色在点击时加载

      ```html
      <el-button type="primary" icon="search" :plain="true">搜索</el-button>
      ```

   4. 图标按钮

      设置对应的icon属性就可以在图标中插入图片

      * 左边

        ```html
        <el-button type="primary" icon="search">搜索</el-button>
        ```

      * 右边

        ```html
        <el-button type="primary" icon="search" :disabled='true'>搜索<i class='el-icon-upload'></i></i></el-button>
        ```

   5. 按钮组合

      一批按钮成队出现，我们可以将其组织在一起

      使用<el-button-group>嵌套我们的<el-button>标签

      ```html
      <el-button-group>
        <el-button type="primary" icon="arrow-left">上一页</el-button>
        <el-button type="primary">下一页<i class="el-icon-arrow-right el-icon--right"></i></el-button>
      </el-button-group>
      <el-button-group>
        <el-button type="primary" icon="edit"></el-button>
        <el-button type="primary" icon="share"></el-button>
        <el-button type="primary" icon="delete"></el-button>
      </el-button-group>
      ```

   6. 加载中动画

      ```html
      <el-button type="primary" :loading="true">加载中</el-button>
      ```

   7. 大小

      使用size属性进行设置

      * large
      * small
      * mini

      ```html
      <el-button type="primary" size="large">大型按钮</el-button>
      <el-button type="primary">正常按钮</el-button>
      <el-button type="primary" size="small">小型按钮</el-button>
      <el-button type="primary" size="mini">超小按钮</el-button>
      ```

# TO BE CONTINUED ...  剩下的详见官方文档

