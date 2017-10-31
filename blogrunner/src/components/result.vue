<template>
  <el-table
    :data='tabledata'
    style="width: 100%"
    >
    <el-table-column
      prop="name"
      label="名称"
      width="180"
    >
    </el-table-column>
    <el-table-column
      prop="md5url"
      label="散列代码"
      width="180"
    >
    </el-table-column>
    <el-table-column
      prop="size"
      label="字数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_reader"
      label="阅读量"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_like"
      label="好评数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_code"
      label="代码数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_photo"
      label="图片数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_link"
      label="链接数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="grade"
      label="评分"
      width="180"
    >
      <template slot-scope="scope">
        <el-rate v-model="scope.row.grade"></el-rate>
      </template>
    </el-table-column>
    <el-table-column
      prop="grade"
      label="测试评分变动"
      width="180"
    >
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  data () {
    return {
      tabledata: [{
        name: '二叉树',
        grade: 3,
        size: 1024,
        number_reader: 3019,
        number_like: 4,
        md5url: '123465742324354sfde242',
        number_code: 3,
        number_photo: 2,
        number_link: 1
      }, {
        name: '二叉树',
        grade: 3,
        size: 1024,
        number_reader: 3019,
        number_like: 4,
        md5url: '123465742324354sfde242',
        number_code: 3,
        number_photo: 2,
        number_link: 1
      }, {
        name: '二叉树',
        grade: 3,
        size: 1024,
        number_reader: 3019,
        number_like: 4,
        md5url: '123465742324354sfde242',
        number_code: 3,
        number_photo: 2,
        number_link: 1
      }]
    }
  }
}
</script>
<style>
</style>
