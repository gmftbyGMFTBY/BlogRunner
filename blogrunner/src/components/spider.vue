<template>
  <div>
    <el-container>
      <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
        <el-menu
          :default-active="activemode"
          mode='vertical'
          background-color="#545c64"
          text-color="#fff"
          active-text-color="#ffd04b"
          >
            <el-menu-item index="1"><router-link to="/website">  站点爬虫</router-link></el-menu-item>
            <el-menu-item index="2"><router-link to="/keyword">关键字爬虫</router-link></el-menu-item>
          </el-menu>
        </el-aside>
      <el-container>
        <el-col :span="20"><router-view></router-view></el-col>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activemode: '1'
    }
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
