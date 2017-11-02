<template>
  <el-upload
    class="upload-demo"
    drag
    action="http://127.0.0.8:8888/htmlupload"
    multiple
    >
    <i class="el-icon-upload"></i>
    <div class="el-upload__text">上传文档</div>
    <div class="el-upload__tip" slot="tip">请上传HTML文档用于检验</div>
  </el-upload>
</template>
<script>
export default {
  data () {
  },
  computed: {
  },
  methods: {
    /*
       upload_the_file () {
      var filedata = document.querySelector('.el-upload .el-upload__input')
      console.log(filedata)
    }
    */
  }
}
</script>
<style>
</style>
