<template>
  <div id="app">
  <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" theme="dark">
  <el-menu-item index="0"><router-link to="/About"><img src="./assets/mylogo.jpg" height="50" width="50">
  </router-link></el-menu-item>
  <el-menu-item index="1"><router-link to="/">主页</router-link></el-menu-item>
  <el-menu-item index="2"><router-link to="/About">关于我们</router-link></el-menu-item>
  <el-menu-item index="3"><router-link to="/Result">结果</router-link></el-menu-item>
   <el-menu-item index="4"><el-input  placeholder="请输入音乐名" icon="search" v-model="mytext" @click="handle"></el-input></el-menu-item>
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
    }
  },
  methods: {
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #20A0FF;
  width:100%;
}
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active for below version 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
