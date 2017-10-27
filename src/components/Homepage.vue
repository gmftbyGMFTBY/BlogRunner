<template>
    <el-row class="search" >
        <el-input 
  size="large"
  placeholder="请输入音乐名"
   v-model="input2"
   icon='search'
    :on-icon-click="handleIconClick">
</el-input> 

</el-row>
</template>
<script>
export default {
  data () {
    return {
      input2: ''
    }
  },
  methods: {
    handleIconClick (ev) {
      console.log(this.input2)
    }
  }
}
</script>

<style>
    body {
  background-image: url('../assets/下载.jpg');
  background-size:cover;
  width:100%;
  height:100%;
}
.search-wrapper {
  width: 100%;
  height: 100%;
}
   .search {
  padding: 300px;
  width:80%;
  margin: auto;

   }
</style>
