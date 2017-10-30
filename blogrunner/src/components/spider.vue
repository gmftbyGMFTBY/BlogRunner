<template>
  <div>
    <el-tabs v-model="activeName">
        <el-tab-pane label="站点爬虫" name="first">站点爬虫</el-tab-pane>
        <el-tab-pane label="关键字爬虫" name="second">关键字爬虫</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  data () {
    return {
      activeName: 'first'
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
