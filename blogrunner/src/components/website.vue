<template>
 <el-form ref="form" :model="form" label-width="80px" size="mini">
   <el-form-item label="用户名">
     <el-input v-model="form.name" size='mini' maxlength="20"></el-input>
   </el-form-item>
   <el-form-item label="页面限制">
     <el-input v-model="form.limit" size='mini' maxlength="5"></el-input>
   </el-form-item>
   <el-form-item>
     <el-button type="primary" @click="submit">搜索</el-button>
   </el-form-item>
 </el-form>
</template>
<script>
export default {
  data () {
    return {
      form: {
        name: '',
        limit: ''
      }
    }
  }
}
</script>
<style>
</style>
