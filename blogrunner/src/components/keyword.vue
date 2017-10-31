<template>
 <el-form ref="form" :model="form" label-width="80px">
   <el-form-item label="关键字">
     <el-input v-model="form.name"></el-input>
   </el-form-item>
   <el-form-item label="页面限制">
     <el-input v-model="form.limit"></el-input>
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
