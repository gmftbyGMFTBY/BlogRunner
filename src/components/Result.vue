<template>
<div>
<el-tabs v-model="activeName" @tab-click="handleClick"
type="border-card">
    <el-tab-pane label="热门评论" name="first">热门评论</el-tab-pane>
    <el-tab-pane label="好评" name="second">好评</el-tab-pane>
    <el-tab-pane label="差评" name="third">差评</el-tab-pane>
    <el-tab-pane label="评论概要" name="fourth">评论概要</el-tab-pane>
  <el-table
    :data="tableData3"
    border
    style="width: 100%">
    <el-table-column
      prop="date"
      label="日期"
      width="180">
    </el-table-column>
    <el-table-column
      prop="name"
      label="用户名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="likecount"
      label="点赞数">
    </el-table-column>
        <el-table-column
      prop="content"
      label="评论">
    </el-table-column>
  </el-table>
  </el-tabs>
</div>
</div>
</div>
</template>

<script>
import Aboutus from './Aboutus'
import Homepage from './Homepage'
export default {
  components: {
    component: Aboutus,
    Homepage
  },
  data () {
    return {
      tableData3: [{
        date: '2016-05-03',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-04',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-01',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-08',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-06',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }, {
        date: '2016-05-07',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      }],
      options: [{
        value: '选项1',
        label: '好评'
      }, {
        value: '选项2',
        label: '差评'
      }, {
        value: '选项3',
        label: 'others'
      }],
      value: ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card{
  width:100%;
  height:100%;
  margin:auto;
  padding:0px;
}
.pagination{
  width:100%;
  margin:auto;
  padding-top:50px;
}
.headerword{
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  font: "PingFang SC";
  text-align:center;
}
</style>
