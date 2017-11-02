<template>
  <el-container>
    <el-input v-model="value" placeholder="请输入检测的URL"></el-input> 
    <el-button type='primary' @click='upload'>上传</el-button>
  </el-container>
</template>
<script>
export default {
  data () {
    return {
      value: ''
    }
  },
  methods: {
    upload () {
      var self = this
      self.$http.post('http://127.0.0.8:8888/urlupload', self.value)
      .then(function (response) {
        console.log(response)
        self.$message({
          message: '恭喜你，URL上传成功',
          type: 'success'
        })
        // 之后的返回的关于网页的信息的评价的逻辑
      })
      .catch(function (error) {
        console.log(error)
      })
    }
  }
}
</script>
<style>
</style>
