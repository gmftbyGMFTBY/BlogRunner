<template>
  <el-container class='search'>
    <el-form>
      <el-form-item>
        <a color="red" href="http://github.com/gmftbyGMFTBY/BlogRunner" height="500px">
          <img src="../assets/logo.png">
        </a>
      </el-form-item>
    </el-form>
  </el-container>
</template>
<script>
export default {
  data () {
    return {
      value: '',
      grade: 0
    }
  },
  methods: {
    upload () {
      var self = this
      self.data = JSON.stringify({'grade': self.grade, 'url': self.value})
      self.$http.post('http://127.0.0.8:8888/urlupload', self.data)
      .then(function (response) {
        console.log(response)
        self.result = response.data['result']
        console.log(self.result)
        if (self.result === -1) {
          self.$message.error('抱歉，请键入CSDN博文地址')
        } else {
          self.$message({
            message: '上传成功，预计博文阅读量为' + self.result.toString(),
            type: 'success'
          })
        }
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
body {
  background-image: url('../assets/website.jpg');
  background-size:cover;
  width:100%;
  height:100%;
}
.search {
  padding: 180px;
  width:60%;
  margin: auto;
} 
</style>
