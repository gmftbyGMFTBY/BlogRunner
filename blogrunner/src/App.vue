<template>
  <div id="app">
    <header class="header" :class="{ 'header-fixed' : true }">
    <el-row>
      <el-col :span='24'>
        <el-menu :default-active='4' class='el-menu-demo' mode='horizontal' theme='dark'>
          <el-menu-item index='0'><img src='./assets/logo.png' height="50" width="50"></el-menu-item>
          <el-menu-item index='1'><router-link to='/'>爬虫定义</router-link></el-menu-item>
          <el-menu-item index='2'><router-link to='/result'>结果查询</router-link></el-menu-item>
          <el-menu-item index='3'><router-link to='/check'>用户检测</router-link></el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    </header>
  <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
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
