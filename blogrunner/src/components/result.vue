<template>
  <el-container>
  <el-container>
  <el-table
    :data='fordata'
    style="width: 100%"
    max-height="750"
    tooltip-effect="dark"
    ref="multipleTable"
    @selection-change="selectionchange"
    >
    <el-table-column type='index' width="55"></el-table-column>
    <el-table-column
      prop="blog_name"
      label="名称"
      width="250"
    >
    </el-table-column>
    <!--<el-table-column
      prop="md5url"
      label="散列代码"
      width="200"
    >
    </el-table-column>-->
    <el-table-column
      prop="size"
      label="字数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_reader"
      label="阅读量"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_like"
      label="好评数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_code"
      label="代码数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_photo"
      label="图片数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="number_link"
      label="链接数"
      width="70"
    >
    </el-table-column>
    <el-table-column
      prop="grade"
      label="评分"
      width="180"
    >
      <template slot-scope="scope">
        <el-rate v-model="scope.row.grade"></el-rate>
      </template>
    </el-table-column>
    <el-table-column
      prop="grade"
      label="操作"
      width="200"
    >
      <template slot-scope="scope">
        <el-button type='text' size='mini' @click="confirmgrade(scope.row.md5url , scope.row.grade)">确认评价</el-button>
        <el-button type='text' size='mini' @click="openblog(scope.row.md5url)">打开博文</el-button>
        <el-button type='text' size='mini' @click="deleteblog(scope)">删除博文</el-button>
      </template>
    </el-table-column>
  </el-table>
  </el-container>
  <el-footer>
  </el-footer>
  </el-container>
</template>
<script>
export default {
  data () {
    return {
      tabledata: [{
        'name': '二叉树',
        'grade': 3,
        'size': 1024,
        'number_reader': 3019,
        'number_like': 4,
        'md5url': '123465742324354sfde242ii2381637we',
        'number_code': 3,
        'number_photo': 2,
        'number_link': 1
      }, {
        name: '二叉树',
        grade: 3,
        size: 1024,
        number_reader: 3019,
        number_like: 4,
        md5url: '123465742324354sfde242',
        number_code: 3,
        number_photo: 2,
        number_link: 1
      }, {
        'name': '二叉树',
        grade: 3,
        size: 1024,
        number_reader: 3019,
        number_like: 4,
        md5url: '123465742324354sfde242',
        number_code: 3,
        number_photo: 2,
        number_link: 1
      }],
      done: false,
      delete: false,
      chooselist: [],
      chooselength: 0
    }
  },
  computed: {
    fordata () {
      console.log(this.$store.state.data)
      return this.$store.state.data
    }
  },
  methods: {
    grade_success () {
      this.$message({
        message: '恭喜你，评价成功',
        type: 'success'
      })
    },
    grade_fail () {
      this.$message.error('评价失败，请确认评价信息')
    },
    confirmgrade (a, b) {
      var self = this
      let data = JSON.stringify({'md5url': a, 'grade': b})
      self.$http.post('http://127.0.0.8:8888/blog/comment', data)
      .then(function (response) {
        console.log(response.data)
        self.done = response.data['done']
        if (self.done === true) {
          self.grade_success()
        } else {
          self.grade_fail()
        }
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    openblog (md5url) {
      window.open('http://127.0.0.8:8888/blog/open/' + md5url)
    },
    /*
    selectionchange: function (val) {
      var arr = []
      val.forEach(function (item) {
        arr.push(item.id)
      })
      this.chooselist = arr
      this.chooselength = this.chooselist.length
    }
    */
    delete_success () {
      this.$message({
        message: '恭喜你，删除成功',
        type: 'success'
      })
    },
    delete_fail () {
      this.$message.error('对不起,删除失败')
    },
    deleteblog (scope) {
      var self = this
      var md5url = scope.row.md5url
      self.$http.post('http://127.0.0.8:8888/blog/delete/' + md5url)
      .then(function (response) {
        self.delete = response.data['delete']
        if (self.delete === true) {
          self.delete_success()
        } else {
          self.delete_fail()
        }
        // 删除当前表表格项 , scope.$index 获取当前的标号
        delete self.$store.state.data[scope.$index]
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
