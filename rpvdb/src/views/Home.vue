<template>
    <div class="home">
        <el-container style="height:100%">
            <el-header>
                <div>
                    <el-tabs type="border-card" value="first"
                             @tab-click="toAnother"
                             :before-leave="beforeLeaveTab">
                        <el-tab-pane label="仿真案例管理" name="first">
                            <el-row :gutter="20">
                                <el-col :span="11" style="border-right: 3px solid #C0C0C0">
                                    <h5><i class="el-icon-search"></i>&nbsp;&nbsp;查看案例</h5>
                                    <span>
                                        <el-row>
                                            <el-col :span="6" :offset="3">
                                                <el-button type="text" @click="datastyle=1"
                                                           :disabled="limit1"> 球形顶盖 </el-button>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-button type="text" @click="datastyle=2"
                                                           :disabled="limit1"> 内带平台球形顶盖 </el-button>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-button type="text" @click="datastyle=3"
                                                           :disabled="limit1"> 平顶盖 </el-button>
                                            </el-col>
                                        </el-row>
                                    </span>
                                </el-col>
                                <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                    <p style="padding:0;margin:0;">
                                        <el-button type="text"
                                                   icon="el-icon-plus"
                                                   style="font-size:30px;"
                                                   @click="dialogVisible1=true"
                                                   :disabled="limit2"
                                                   title="create"></el-button>
                                        <span style="font-size: 14px; color:cadetblue">
                                            &nbsp;&nbsp;&nbsp;&nbsp;新建
                                        </span>
                                    </p>
                                    <el-dialog title="新建案例"
                                               :visible.sync="dialogVisible1"
                                               width="80%">
                                        <CreateCase></CreateCase>
                                    </el-dialog>
                                </el-col>
                                <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                    <p style="padding:0;margin:0;">
                                        <el-button type="text" icon="el-icon-delete"
                                                   style="font-size:30px;"
                                                   :disabled="viewIndex.index=='' || limit2"
                                                   @click="deleteCase"
                                                   title="delete"></el-button>
                                        <span style="font-size: 14px; color:cadetblue">
                                            &nbsp;&nbsp;&nbsp;&nbsp;删除
                                        </span>
                                    </p>
                                </el-col>
                                <el-col :span="4">
                                    <p style="padding:0;margin:0;">
                                        <el-button type="text" icon="el-icon-search"
                                                   style="font-size:30px;"
                                                   @click="dialogVisible2=true"
                                                   :disabled="limit1"></el-button>
                                        <span style="font-size: 14px; color:cadetblue">
                                            &nbsp;&nbsp;&nbsp;&nbsp;检索匹配
                                        </span>
                                    </p>
                                    <el-dialog title="检索匹配"
                                               :visible.sync="dialogVisible2"
                                               width="80%">
                                        <Search @show-case="showCase"></Search>
                                    </el-dialog>
                                </el-col>
                            </el-row>
                        </el-tab-pane>
                        <el-tab-pane label="数据库管理" name="second">
                        </el-tab-pane>
                    </el-tabs>
                    <div class="user">
                        <el-popover trigger="hover">
                            <template #reference>
                                <el-avatar shape="square" size="medium" fit="fill" :src="url"></el-avatar>
                            </template>
                            <template #default>
                                <p class="user-name" >{{logName}}({{users}})</p>
                                <div style="position:relative; margin-left:30%">
                                    <el-button margin-left="50%" size="small" type="primary" @click="logoff">注销</el-button>
                                </div>                       
                            </template>
                        </el-popover>
                    </div>
                </div>
            </el-header>
            <br /><br /><br /><br />
            <el-container>
                <el-aside width="12%" style="border-right: 2px solid #C0C0C0">
                    <div style="height:40em">
                        <p style="margin:0;line-height:16px;text-align:right">
                            <span class="list-title">
                                {{showtitle}}
                            </span>
                            <span>
                                <el-button v-show="datastyle" type="text"
                                           @click="reset" icon="el-icon-close"
                                           :class="[datastyle==2 ? 'title2':'title1']"></el-button>
                            </span>
                        </p>
                        <ViewAside :dataStyle="datastyle" v-if="datastyle && datastyle!=7"
                                   @show-detail="viewIndex=$event"></ViewAside>
                        <SearchCase :caselist="searchlist" v-if="datastyle==7" 
                                    @show-detail="viewIndex=$event"></SearchCase>
                    </div>
                </el-aside>
                <el-main>
                    <ViewCase :index="viewIndex" style="line-height:10px"
                              v-if="viewIndex.index"></ViewCase>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style>
    .el-header {
        text-align: center;
        margin-left: 5%;
        margin-right: 5%;
        margin-top: 2%;
        line-height: 100%;
        float: right;
        padding: 0;
    }
    .el-aside {
        margin-left: 5%;
        text-align: center;
        line-height: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        float: right;
        clear:both;
    }
    .el-main {
        margin-right: 21px;
        text-align: center;
        line-height: 160px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        padding-top:10px;
    }
    h5{
        margin-top:4px;
        margin-bottom:4px;
    }
    .el-col-4 {
        line-height:60px;
    }
    .list-title{
        font-size:14px;
        font-weight:700;
        text-align:center;
    }
    .title1 {
        margin-left: 40px;
        margin-right: 10px
    }
    .title2 {
        margin-left: 10px;
        margin-right: 10px
    }
    .user{
        position:absolute;
        margin-right: 2%;
        margin-top: 2%;
    }
    .user-name{
        font-family:'Times New Roman', Times, serif;
        font-weight:bolder;
        text-align: center;
    }
</style>

<script>
    import ViewAside from '../components/ViewAside.vue';
    import ViewCase from '../components/ViewCase.vue';
    import Search from '../components/Search.vue';
    import SearchCase from '../components/SearchCase.vue';
    import CreateCase from '../components/CreateCase.vue';
    import DelectCase from '../components/DelectCase.vue';
    import axios from 'axios';
    export default {
        name: 'Home',
        data() {
            return {
                datastyle: 0,
                viewIndex: {
                    style: this.datastyle,
                    index: '',
                },
                dialogVisible1: false,
                dialogVisible2: false,
                dialogVisible3: false,
                searchlist: [],
                logClass: this.$route.params.logClass,
                logName: this.$route.params.logName,
                limit1: true,
                limit2: true,
                url: require('../../public/R.jpg')
            };
        },

        methods: {
            toAnother(tab) {
                if (tab.name == 'second') {
                    this.$router.push({ name: 'Dataset', params: { logClass: this.logClass, logName: this.logName } });
                }
            },

            beforeLeaveTab(activeName, oldName) {
               return false
            },

            reset() {
                this.datastyle = 0;
            },

            showCase(caselist) {
                this.searchlist = caselist;
                this.datastyle = 7;
                this.dialogVisible2 = false;
            },

            deleteCase() {
                this.$confirm('将永久删除该算例信息与仿真结果, 是否继续?',{
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    let index = this.viewIndex;
                    let style = index.style;
                    const path = 'http://localhost:5000/change/delete';
                    axios.post(path, index)
                        .then(() => {
                            this.reset();
                            this.$nextTick(() => {
                                this.datastyle = style;
                            })
                        })
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    
                });
                
            },

            logoff(){
                this.$router.push({ name: 'Login' });
            }
        },

        computed: {
            showtitle() {
             //显示列表标题
                switch (this.datastyle) {
                    case 1: return ("球形顶盖");
                    case 2: return ("内带平台球形顶盖");
                    case 3: return ("平顶盖");
                    case 7: return ("检索结果");
                }
            },
            users() {
                if (this.logClass == 1) {
                    return '普通用户'
                } else if (this.logClass == 0) {
                    return '管理员'
                }
            }
        },

        watch: {
            datastyle: {
                handler(newstyle, oldstyle) {
                    this.viewIndex = {
                        style: this.datastyle,
                        index: ''
                    }
                }
            },
            logClass: {
                handler(newstyle, oldstyle) {
                    if (newstyle == 0) {
                        this.limit1 = false;
                        this.limit2 = false;
                    } else if (newstyle == 1) {
                        this.limit1 = false;
                    }
                },
                immediate:true
            },
            $route(to,from){
                this.logClass = this.$route.params.logClass;
                this.logName = this.$route.params.logName;
            }
        },

        components: {
            ViewAside,
            ViewCase,
            Search,
            SearchCase,
            CreateCase,
            DelectCase
        },

    }
</script>
