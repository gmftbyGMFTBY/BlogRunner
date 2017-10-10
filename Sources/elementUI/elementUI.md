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

   * gutter属性支持在列级分栏中插入间隔,默认间隔是0

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
        <el-button type="primary" icon="search" :disabled='true'>搜索<i class='el-icon-upload'><i></i></el-button>
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

### 表单

#### 单选框

1. <el-radio>

   属性

   * class : class="radio",radio组件定义
   * v-model : vue的语法，绑定变量
   * label : v-model绑定的时候，如果单选选中的话，绑定的变量的值就是label的值(number / string)，如果我们绑定的变量的初始值和我们的label的值一致的是被选中的选项
   * disabled : disables禁用

   ```html
   <template>
     <el-radio disabled class="radio" v-model="radio" label="1">备选项</el-radio>
     <el-radio class="radio" v-model="radio" label="2">备选项</el-radio>
   </template>

   <script>
     export default {
       data () {
         return {
           radio: '1'
         };
       }
     }
   </script>
   ```

2. <el-radio-group>

   单选框组，在el-radio-group张可以绑定统一的变量

   属性

   * v-model :　绑定单选组的统一变量
   * change : 相应变化属性，和函数绑定，参数是选中的label的值

   ```html
   <template>
     <el-radio-group v-model="radio2">
       <el-radio :label="3">备选项</el-radio><!-- 这里的label前面要用:来标定 -->
       <el-radio :label="6">备选项</el-radio>
       <el-radio :label="9">备选项</el-radio>
     </el-radio-group>
   </template>

   <script>
     export default {
       data () {
         return {
           radio2: 3
         };
       }
     }
   </script>
   ```

3. <el-radio-button>

   修改单选的样式成为按钮

   属性

   * size : 默认 , large , small

#### 多选框

单独使用可以再选中和不选中中之间切换

1. <el-chekcbox>

   * v-model : checkbox是多选框属性
   * disables : 禁用和不禁用
   * label : 同上
   * indeterminate : 表示不确定状态，可以用来实现全选效果

2. <el-checkbox-group>

   属性

   * min / max : 选中数目限制

     ```html
     <template>
       <el-checkbox-group 
         v-model="checkedCities1"
         :min="1"
         :max="2">
         <el-checkbox v-for="city in cities" :label="city" :key="city">{{city}}</el-checkbox>
       </el-checkbox-group>
     </template>
     <script>
       const cityOptions = ['上海', '北京', '广州', '深圳'];
       <!-- 在template中可以使用元素的话，我们必须将值放到export的data中去return才可以 -->
       export default {
         data() {
           return {
             checkedCities1: ['上海', '北京'],
             cities: cityOptions
           };
         }
       };
     </script>
     ```

     ​

   可以管理很多的单选框，只要v-model属性绑定的是我们的array的列表属性即可

   ```html
   <template>
     <el-checkbox-group v-model="checkList">
       <el-checkbox label="复选框 A"></el-checkbox><!-- 选中 -->
       <el-checkbox label="复选框 B"></el-checkbox>
       <el-checkbox label="复选框 C"></el-checkbox>
       <el-checkbox label="禁用" disabled></el-checkbox>
       <el-checkbox label="选中且禁用" disabled></el-checkbox>
     </el-checkbox-group>
   </template>

   <script>
     export default {
       data () {
         return {
           checkList: ['选中且禁用','复选框 A']
         };
       }
     };
   </script>
   ```

3. <el-checkbox-button>

   同上

#### 输入框

1. <el-input>

   * v-model : 绑定变量，显示初始字符串

   * placeholder : 字符串，显示提示词

   * disabled : 禁用

   * icon : 添加el-icon-iconName可以实现添加图标

   * on-icon-click : 对icon的事件绑定

   * type : type="textarea"是文本域的模式

     * row : 可以控制文本域的高度

   * autosize :

     可以自动的控制高度，并且可以控制最大最小行数

     ```html
     <el-input
       type="textarea"
       :autosize="{ minRows: 2, maxRows: 4}"
       placeholder="请输入内容"
       v-model="textarea3">
     </el-input>
     ```

   * slot :

     在<el-input>内部可以嵌套其他的HTML或者elementui的元素，并且在其中可以添加slot属性用来表示在文本框中的前后预制的内容

     * prepend : 前置
     * append : 后置

   * size 

     调整大小large / small / mini

   ```html
   <el-input
     placeholder="请选择日期"
     icon="search"
     v-model="input2"
     :on-icon-click="handleIconClick">
   </el-input>

   <script>
   export default {
     data() {
       return {
         input2: ''
       }
     },
     methods: {
       handleIconClick(ev) {
         console.log(ev);
       }
     }
   }
   </script>
   ```

2. <el-autocomplete>

   带有输入建议的输入框组件

#### 计数器

1. <el-input-number>
   * v-model : 绑定变量，变量的值是初始值
   * min : 最小下线
   * max : 最大上限
   * @change : 绑定函数
   * disabled : 禁用
   * step : 步长
   * size : 大小

#### 选择器

1. <el-select>

   * v-model

   * placeholder

   * disabled : 整体禁用

   * clearable : 当输入框中存在值的时候，后面有一个叉号按钮点击可以清空

   * multiple : 多选

   * filterable : 过滤器，可以启动搜索

   * 自定义

     ```html
     <template>
       <el-select v-model="value6" placeholder="请选择">
         <el-option
           v-for="item in cities"
           :key="item.value"
           :label="item.label"
           :value="item.value">
           <span style="float: left">{{ item.label }}</span>
           <span style="float: right; color: #8492a6; font-size: 13px">{{ item.value }}</span>
         </el-option>
       </el-select>
     </template>
     ```

2. <el-option>

   * label : v-model的绑定的值就是label的值
   * disabled : 禁用

3. <el-option-group>

   对选项进行分组

   ```html
   <template>
     <el-select v-model="value7" placeholder="请选择">
       <el-option-group
         v-for="group in options3"
         :key="group.label"
         :label="group.label">
         <el-option
           v-for="item in group.options"
           :key="item.value"
           :label="item.label"
           :value="item.value">
         </el-option>
       </el-option-group>
     </el-select>
   </template>
   ```

#### 级联选择器

当一个数据集合有清晰的层级结构时，可通过级联选择器逐级查看并选择。

1. <el-cascader>

   * options : 制定嵌套的JSON来实现级联选择器

     嵌套额时候JSON使用children作为键来嵌套

   * `options`指定的数组中的第一个元素含有`disabled: true`键值对，因此是禁用的

   * show-all-levels : 如果是false的话，我们只保留最后一集目录

   * v-model : 绑定变量，顺便可以实现默认值

   * change-on-select : 允许给用户动态的显示选择的路径情况

   * filterable : 搜索

#### 开关

1. <el-switch>
   * v-model
   * on-text
   * off-text
   * on-color
   * off-color
   * on-value : boolean , string , number
   * off-value : boolean , string , number
   * disabled

#### 滑块

1. <el-slider>
   * v-model : 绑定一个值，现实滑块的百分比使用程度
   * disabled : 禁用
   * show-tooltip : 绑定一个函数可以格式化自定义我们的tooltip,一个函数返回一个值显示tooltip上
   * step : 变化是跳跃离散的
   * show-step : 显示断点的离散点
   * show-input : 在show-input弧线是一个输入框，点击调整我们的滑块的位置

#### 时间选择器

1. <el-time-select>

   * v-model

   * placeholder

   * picker-options

     * start

     * step

     * end

     * 随意时间

       ```html
       <template>
         <el-time-picker
           v-model="value2"
           :picker-options="{
             selectableRange: '18:30:00 - 20:30:00'
           }"
           placeholder="任意时间点">
         </el-time-picker>
       </template>
       ```

2. <el-date-picker>

   * type : 制定基本的时间单位 / date

#### 上传

通过点击或者拖拽上传文件

http://element.eleme.io/#/zh-CN/component/upload

#### 评分

1. <el-rate>

   评分被分为三个等级，可以利用颜色对分数及情感倾向进行分级

   * v-model : 

   * colors : 

     三个值的列表

     * low-shreshold : 阈值
     * high-shreshold : 阈值

   * show-text

     为组件设置 `show-text` 属性会在右侧显示辅助文字。通过设置 `texts` 可以为每一个分值指定对应的辅助文字。`texts` 为一个数组，长度应等于最大值 `max`。

   * disabled : 只读的评分系统，允许出现小数

#### 颜色选择器

用于颜色选择，支持多种格式

1. <el-color-picker>
   * v-model : 和字符串变量绑定，选定颜色
   * show-alpha : 选择透明度选项打开

#### Form表单

由输入框、选择器、单选框、多选框等控件组成，用以收集、校验、提交数据

在 Form 组件中，每一个表单域由一个 Form-Item 组件构成，表单域中可以放置各种类型的表单控件，包括 Input、Select、Checkbox、Radio、Switch、DatePicker、TimePicker	

1. <el-form>
   * inline : 行内表单
2. <el-form-item>
   * label : 显示的提示文字

```html
<el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="活动名称">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="活动区域">
    <el-select v-model="form.region" placeholder="请选择活动区域">
      <el-option label="区域一" value="shanghai"></el-option>
      <el-option label="区域二" value="beijing"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="活动时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
  <el-form-item label="即时配送">
    <el-switch on-text="" off-text="" v-model="form.delivery"></el-switch>
  </el-form-item>
  <el-form-item label="活动性质">
    <el-checkbox-group v-model="form.type">
      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
      <el-checkbox label="地推活动" name="type"></el-checkbox>
      <el-checkbox label="线下主题活动" name="type"></el-checkbox>
      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源">
    <el-radio-group v-model="form.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="活动形式">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
```

### 表格

用于展示多条结构类似的数据，可对数据进行排序、筛选、对比或其他自定义操作。

1. <el-table>

   * data
   * style
   * height : 固定表头

2. <el-table-column>

   * prop

   * label

   * width

   * fixed : 固定列　left / right

   * type : 实现多选非常简单: 手动添加一个`el-table-column`，设`type`属性为`selection`即可

   * sortable : 支持排序的列，排序是整行移动的

   * filters : 开启过滤，显示text

   * filter-method :

     在列中设置`filters`,`filter-method`属性即可开启该列的筛选，`filters 是一个数组，`filter-method`是一个方法，它用于决定某些数据是否显示，会传入两个参数：`value`和`row

     ```html
     <template>
       <el-table
         :data="tableData"
         border
         style="width: 100%">
         <el-table-column
           prop="date"
           label="日期"
           sortable
           width="180">
         </el-table-column>
         <el-table-column
           prop="name"
           label="姓名"
           width="180">
         </el-table-column>
         <el-table-column
           prop="address"
           label="地址"
           :formatter="formatter">
         </el-table-column>
         <el-table-column
           prop="tag"
           label="标签"
           width="100"
           :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]"
           :filter-method="filterTag"
           filter-placement="bottom-end">
           <template scope="scope">
             <el-tag
               :type="scope.row.tag === '家' ? 'primary' : 'success'"
               close-transition>{{scope.row.tag}}</el-tag>
           </template>
         </el-table-column>
       </el-table>
     </template>

     <script>
       export default {
         data() {
           return {
             tableData: [{
               date: '2016-05-02',
               name: '王小虎',
               address: '上海市普陀区金沙江路 1518 弄',
               tag: '家'
             }, {
               date: '2016-05-04',
               name: '王小虎',
               address: '上海市普陀区金沙江路 1517 弄',
               tag: '公司'
             }, {
               date: '2016-05-01',
               name: '王小虎',
               address: '上海市普陀区金沙江路 1519 弄',
               tag: '家'
             }, {
               date: '2016-05-03',
               name: '王小虎',
               address: '上海市普陀区金沙江路 1516 弄',
               tag: '公司'
             }]
           }
         },
         methods: {
           formatter(row, column) {
             return row.address;
           },
           filterTag(value, row) {
             return row.tag === value;
           }
         }
       }
     </script>

     ```

   * 自定义列模板

     自定义列的显示内容，可组合其他组件使用。通过 `Scoped slot` 可以获取到 row, column, $index 和 store（table 内部的状态管理）的数据

     ```html
     <el-table-column label="操作">
           <template scope="scope">
             <el-button
               size="small"
               @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
             <el-button
               size="small"
               type="danger"
               @click="handleDelete(scope.$index, scope.row)">删除</el-button>
           </template>
         </el-table-column>
     ```

```html
  <template>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="date"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址"><!-- 长度默认了 -->
      </el-table-column>
    </el-table>
  </template>

  <script>
    export default {
      data() {
        return {
          tableData: [{
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
        }
      }
    }
  </script>

```

### 标签

用于标记和选择。

1. <el-tag>

   * closable : 可关闭的标签

   ```html
   <el-tag>标签一</el-tag>
   <el-tag type="gray">标签二</el-tag>
   <el-tag type="primary">标签三</el-tag>
   <el-tag type="success">标签四</el-tag>
   <el-tag type="warning">标签五</el-tag>
   <el-tag type="danger">标签六</el-tag>
   ```

### 分页

<el-pagination>

* layout
  * prev : 上一页
  * next : 下一页
  * pager : 页码列表
* total : total / 10 代表一次最多显示的页数
* small : 小型分页

### 提示

用于在页面显示重要的提示信息

1. <el-alert>

   * title :  文字
   * type : 种类，成功，错误等
   * show-icon : 可以现实对应的type的icon
   * description : 显示描述文字

   ```html
     <el-alert
       title="成功提示的文案"
       type="success"
       show-icon
       description>
     </el-alert>
   ```

2. 加载

   ```html
   <template>
     <el-button
       type="primary"
       @click="openFullScreen"
       element-loading-text="拼命加载中"
       v-loading.fullscreen.lock="fullscreenLoading">
       显示整页加载，3 秒后消失
     </el-button>
   </template>

   <script>
     export default {
       data() {
         return {
           fullscreenLoading: false
         }
       },
       methods: {
         openFullScreen() {
           this.fullscreenLoading = true;
           setTimeout(() => {
             this.fullscreenLoading = false;
           }, 3000);
         }
       }
     }
   </script>
   ```

3. 提示

   ```html
   <template>
     <el-button :plain="true" @click="open5">消息</el-button>
     <el-button :plain="true" @click="open6">成功</el-button>
     <el-button :plain="true" @click="open7">警告</el-button>
     <el-button :plain="true" @click="open8">错误</el-button>
   </template>

   <script>
     export default {
       methods: {
         open5() {
           this.$message({
             showClose: true,
             message: '这是一条消息提示'
           });
         },

         open6() {
           this.$message({
             showClose: true,
             message: '恭喜你，这是一条成功消息',
             type: 'success'
           });
         },

         open7() {
           this.$message({
             showClose: true,
             message: '警告哦，这是一条警告消息',
             type: 'warning'
           });
         },

         open8() {
           this.$message({
             showClose: true,
             message: '错了哦，这是一条错误消息',
             type: 'error'
           });
         }
       }
     }
   </script>
   ```

4. 弹框

   调用`$alert`方法即可打开消息提示，它模拟了系统的 `alert`，无法通过按下 ESC 或点击框外关闭。此例中接收了两个参数，`message`和`title`。值得一提的是，窗口被关闭后，它默认会返回一个`Promise`对象便于进行后续操作的处理。若不确定浏览器是否支持`Promise`，可自行引入第三方 polyfill 或像本例一样使用回调进行后续处理。

   ```html
   <template>
     <el-button type="text" @click="open">点击打开 Message Box</el-button>
   </template>

   <script>
     export default {
       methods: {
         open() {
           this.$alert('这是一段内容', '标题名称', {
             confirmButtonText: '确定',
             //之后点击确认后的返回结果
             callback: action => {//action表示确认，下面用到了
               this.$message({
                 type: 'info',
                 message: `action: ${ action }`
               });
             }
           });
         }
       }
     }
   </script>

   ```

### 导航

1. <el-menu>

   * mode : 水平还是竖直
   * collapse : 决定是否折叠

2. <el-menu-item>

3. <el-submenu>

   生成二级菜单