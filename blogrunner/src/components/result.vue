<template>
  <el-container>
  <el-container>
  <el-table
    :data='filterfordata'
    style="width: 100%"
    max-height="500"
    tooltip-effect="dark"
    ref="multipleTable"
    @selection-change="selectionchange"
    >
    <el-table-column type='index' width="55"></el-table-column>
    <el-table-column
      v-if="show"
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
    按照评价信息筛选&nbsp;&nbsp;
    <el-select v-model="currenttype" placeholder="按照评价筛选" size="small">
      <el-option
        v-for="type in types"
        :value="type">
      </el-option>
    </el-select>
    <el-button type="primary" @click="batchdelete">批量删除</el-button>
    <el-button type="primary" @click="searchhistory">历史记录</el-button>
    <el-button type="primary" @click="train">重新训练</el-button>
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
      chooselength: 0,
      currenttype: 'All',
      types: ['All', 0, 1, 2, 3, 4, 5],
      show: true
    }
  },
  computed: {
    fordata () {
      console.log(this.$store.state.data)
      return this.$store.state.data
    },
    filterfordata () {
      var self = this
      var type = self.currenttype
      return self.$store.state.data.filter(function (data) {
        if (type === 'All') {
          // 全部都显示
          return true
        } else {
          // 否则显示指定的部分
          return data.grade === type
        }
      })
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
      console.log('delete!')
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
        self.$store.state.data.splice(scope.$index, 1)
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    batchdelete () {
      var self = this
      var type = self.currenttype
      var len = self.$store.state.data.length
      var p = 1
      for (var i = 0, flag = true; i < len; flag ? i++ : i) {
        if (self.$store.state.data[i].grade === type) {
          self.$store.state.data.splice(i, 1)
          flag = false
          var md5url = self.$store.state.data[i]['md5url']
          self.$http.post('http://127.0.0.8:8888/blog/delete/' + md5url)
          .then(function (response) {
            console.log(response)
            if (p === 1) {
              self.delete_success()
              p = p - 1
            }
          })
          .catch(function (error) {
            console.log(error)
          })
        } else {
          flag = true
        }
      }
    },
    searchhistory () {
      var self = this
      self.$http.post('http://127.0.0.8:8888/history')
      .then(function (response) {
        self.$store.state.data = response.data
        self.show = false
      })
      .catch(function (error) {
        console.log(error)
      })
    },
    train () {
      var self = this
      self.$http.post('http://127.0.0.8:8888/train')
      .then(function (response) {
        console.log(response)
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
