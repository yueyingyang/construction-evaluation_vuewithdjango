<template> 
    <div>
        <el-row>
            <el-button size="small" class='btn' @click="next">下一步</el-button>
            <el-button size="small" class='btn' @click="back">上一步</el-button>
            <!-- <el-button size="small" class='btn' @click="save1">保存</el-button> -->
        </el-row>
        <el-row :gutter="5">
            <el-col :span="9">
                <h3>基本信息</h3>
                <el-row>
                    <span class="lebal">项目名称</span>
                    <el-input size="small" style="width:200px" v-model="project_name" placeholder="请输入内容"></el-input>
                </el-row>
                <el-row>
                    <span class="lebal">客户名称</span>
                    <el-input size="small" style="width:200px" v-model="client_name" placeholder="请输入内容"></el-input>
                </el-row>
                <el-row>
                    <span class="lebal">项目负责人</span>
                    <el-input size="small" style="width:200px" v-model="project_leader" placeholder="请输入内容"></el-input>
                </el-row>
             </el-col>
        <el-col :span="11">
            <h3>项目说明</h3>
            <el-input
                type="textarea"
                :rows="15"
                placeholder="请输入内容"
                v-model="project_description">
            </el-input>
        </el-col>
        </el-row> 
    </div>
</template>
<script>
export default {
    data(){
        return{
            project_name:'',
            client_name:'',
            project_leader:'',
            project_description:''
        }
    },
    beforeRouteLeave(to, from, next){
    //  if (to.name == 'step2') {
        let project_name = this.project_name
        let client_name = this.client_name
        let project_leader = this.project_leader
        let project_description = this.project_description
        localStorage.setItem('project_name', project_name)
        localStorage.setItem('client_name', client_name)
        localStorage.setItem('project_leader', project_leader)
        localStorage.setItem('project_description', project_description)
        next()
    },
    // beforeCreate()
    // {
    //     let project_name = localStorage.getItem('project_name')
    //     console.log('beforecreated')
    // },
    created(){
      //从localStorage中读取条件并赋值给查询表单
      
        let project_name = localStorage.getItem('project_name')
        console.log(project_name)
        let client_name = localStorage.getItem('client_name')
        console.log(client_name)
        let project_leader = localStorage.getItem('project_leader')
        let project_description = localStorage.getItem('project_description')
        if (project_name != null) {
            this.project_name =project_name
        }
        if (client_name != null) {
            this.client_name = client_name
        }
        if (project_leader != null) {
            this.project_leader = project_leader
        }
        if (project_description != null) {
            this.project_description = project_description
        }
    },
    methods:{
        next(){    
            let _this=this;
            var username=localStorage.getItem('phone')
            this.$ajax({
                method:'get',
                url:'step1',
                params:{
                    username:username,
                    project_name:this.project_name,
                    client_name:this.client_name,
                    project_leader:this.project_leader,
                    project_description:this.project_description,
                    project:localStorage.getItem('project')
                },
                headers:{"Content-Type": "application/json"}
            })
            .then(function(response){
                        console.log(response)
                        var res = response.data
                        console.log(res)
                        if (res['error_num'] == 0) {
                            _this.$message.success(res['msg'])
                            localStorage.setItem('project',res['project'])
                            //_this.$emit('next','');
                            setTimeout(()=>{
                                _this.$emit('next','');
                            },500)
                        } 
                        else {
                            _this.$message.error(res['msg'])
                            console.log(res['msg'])
                        }
                    })
                    .catch(function(err){
                        console.log(err);
                    });
        },
        back(){
            this.$emit('back','');
        },
        // save1(){
        //     let _this=this;
        //     var username=localStorage.getItem('phone')
        //     localStorage.setItem('project_name', this.project_name)
        //     localStorage.setItem('project_leader', this.project_leader)
        //     localStorage.setItem('project_description', this.project_description)
        //     localStorage.setItem('client_name', this.client_name)
        //     this.$ajax({
        //         method:'get',
        //         url:'step1',
        //         params:{
        //             username:username,
        //             project_name:this.project_name,
        //             client_name:this.client_name,
        //             project_leader:this.project_leader,
        //             project_description:this.project_description,
        //             project:localStorage.getItem('project')
        //         },
        //         headers:{"Content-Type": "application/json"}
        //     })
        //     .then(function(response){
        //                 console.log(response)
        //                 var res = response.data
        //                 console.log(res)
        //                 if (res['error_num'] == 0) {
        //                     console.log(res['msg'])
        //                     console.log(localStorage.getItem('project_name'))
        //                     console.log(res['project_leader'])
        //                     console.log(res['project_description'])
        //                     console.log(res['client_name'])
        //                     _this.$message.success(res['msg'])
        //                     localStorage.setItem('project',res['project'])
        //                 } 
        //                 else {
        //                     _this.$message.error(res['msg'])
        //                     console.log(res['msg'])
        //                 }
        //             })
        //             .catch(function(err){
        //                 console.log(err);
        //             });
        // },
    }
}
</script>

<style scoped>
    .lebal{
        display: inline-block;
        padding:12px 0;
        color: #333;
        font-size: 14px;
        width:80px;
        margin-top:10px;
    }
    .btn{
        margin-top:12px;
    }

</style>
