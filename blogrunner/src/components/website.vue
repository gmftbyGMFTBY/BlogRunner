<template>
 <el-form
   v-loading.fullscreen.lock='loading'
   element-loading-text="拼命加载中"
   element-loading-spinner="el-icon-loading"
   element-loading-background="rgba(0, 0, 0, 0.8)"
   ref="form" :model="form" label-width="80px">
   <el-form-item label="用户账号">
     <el-input v-model="form.username"></el-input>
   </el-form-item>
   <el-form-item label="页面限制">
     <el-input v-model="form.limit"></el-input>
   </el-form-item>
   <el-form-item>
     <el-button type="primary" @click="postdata">搜索</el-button>
   </el-form-item>
   <el-form-item>{{result}}</el-form-item>
 </el-form>
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
</style>
