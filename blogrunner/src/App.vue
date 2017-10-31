<template> 
<div id="app">
    <el-menu 
      :default-active="active1"
      mode='horizontal'
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="1"><img src='./assets/logo.png' height="12.5" width="12.5"></el-menu-item>
        <el-submenu index="2">
          <template slot="title">爬虫定义</template>
            <el-menu-item index="2-1"><router-link to="/keyword">关键字爬虫</router-link></el-menu-item>
            <el-menu-item index="2-2"><router-link to="/website">用户爬虫</router-link></el-menu-item>
        </el-submenu>
      <el-menu-item index="3"><router-link to="/result">结果查询</router-link></el-menu-item>
      <el-submenu index="4">
        <template slot="title">用户检测</template>
          <el-menu-item index="4-1"><router-link to="/urlupload">URL上传</router-link></el-menu-item>
          <el-menu-item index="4-2"><router-link to="/htmlupload">网页上传</router-link></el-menu-item>
      </el-submenu>
    </el-menu>
    <router-view></router-view>
  </div>
</template>
<script>
export default {
  component: {
  },
  data () {
    return {
      active1: true
    }
  },
  methods: {
  }
}
</script>

<style>
#app {
  min-width: 1200px;
  margin: 0 auto;
  font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
}
.slide-fade-enter-active {
  trasition: all .3s ease;
}
.slide-fade-leave-active {
  trasition: all .8s cubic-bezier(1.0 0.5 0.8 1.0);
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}

/* 头部导航 */
header{z-index: 1000;min-width: 1200px;transition: all 0.5s ease;  border-top: solid 4px #3091F2;  background-color: #fff;  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);  }
header.header-fixed{position: fixed;top: 0;left: 0;right: 0;}
header.el-menu-demo{padding-left: 300px!important;}
</style>
