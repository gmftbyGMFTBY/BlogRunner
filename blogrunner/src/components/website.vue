<template>
 <el-container class="search">
 <el-form
   v-loading.fullscreen.lock='loading'
   element-loading-text="拼命加载中"
   element-loading-spinner="el-icon-loading"
   element-loading-background="rgba(0, 0, 0, 0.8)"
   ref="form" :model="form" label-width="80px">
   <el-form-item>
     <el-input v-model="form.username" placeholder="请输入要查询的用户"></el-input>
   </el-form-item>
   <el-form-item>
     <el-input v-model="form.limit" placeholder="页面限制数目"></el-input>
   </el-form-item>
   <el-form-item>
     <el-button type="primary" @click="postdata">搜索</el-button>
   </el-form-item>
 </el-form>
 </el-container>
</template>
<script>
export default {
  data () {
    return {
      form: {
        username: '',
        limit: ''
      },
      result: [],
      loading: false
    }
  },
  methods: {
    /*
    postdata () {
      this.$http({
        method: 'post',
        url: 'http://127.0.0.8:8888/spider/keyword',
        data: {
          'username': 'gmftby',
          'limit': 2
        }
      })
    }
    */
    postdata () {
      var self = this
      let data = JSON.stringify(this.form)
      self.loading = true
      self.$http.post('http://127.0.0.8:8888/spider/website', data)
      .then(function (response) {
        self.result = response.data
        self.loading = false
        self.$store.state.data = self.result
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
