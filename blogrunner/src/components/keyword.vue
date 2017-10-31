<template>
 <el-form ref="form" :model="form" label-width="80px">
   <el-form-item label="关键字">
     <el-input v-model="form.name"></el-input>
   </el-form-item>
   <el-form-item label="页面限制">
     <el-input v-model="form.limit"></el-input>
   </el-form-item>
   <el-form-item>
     <el-button type="primary" @click="postdata">搜索</el-button>
   </el-form-item>
 </el-form>
</template>
<script>
export default {
  data () {
    return {
      form: {
        keyword: '',
        limit: ''
      }
    }
  },
  methods: {
    /*
    postdata () {
      this.$http({
        method: 'post',
        url: 'http://127.0.0.8:8888/spider/keyword',
        data: {
          'keyword': 'gmftby',
          'limit': 2
        }
      })
    }
    */
    postdata () {
      let data = "{'keyword': 'gmftby' , 'limit': 2}"
      this.$http.post('http://127.0.0.8:8888/spider/keyword', data)
      .then(function (response) {
        console.log(response)
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
