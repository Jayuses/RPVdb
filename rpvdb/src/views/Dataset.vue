<template>
    <div class="dataset">
        <el-container style="height:100%">
            <el-header>
                <div>
                    <el-tabs type="border-card" value="second"
                             :before-leave="beforeLeaveTab"
                             @tab-click="toAnother">
                        <el-tab-pane label="仿真案例管理" name="first">
                        </el-tab-pane>
                        <el-tab-pane label="数据库管理" name="second">
                            <el-col :span="11" style="border-right: 3px solid #C0C0C0">
                                <h5>&nbsp;&nbsp;查看数据库</h5>
                                <span>
                                    <el-row>
                                        <el-col :span="6" :offset="3">
                                            <el-button type="text" @click="datastyle=4"
                                                       :disabled="limit1"> 结构尺寸库 </el-button>
                                        </el-col>
                                        <el-col :span="6">
                                            <el-button type="text" @click="datastyle=5"
                                                       :disabled="limit1"> 结构材料库 </el-button>
                                        </el-col>
                                        <el-col :span="6">
                                            <el-button type="text" @click="datastyle=6"
                                                       :disabled="limit1"> 加载工况库 </el-button>
                                        </el-col>
                                    </el-row>
                                </span>
                            </el-col>
                            <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                <p style="padding:0;margin:0;">
                                    <el-button type="text" icon="el-icon-plus" style="font-size:30px;"
                                               :disabled="limit2 || viewIndex.index=='' "
                                               @click="operation='create'"></el-button>
                                    <span style="font-size: 14px; color:cadetblue">
                                        &nbsp;&nbsp;&nbsp;&nbsp;新建
                                    </span>
                                </p>
                            </el-col>
                            <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                <p style="padding:0;margin:0;">
                                    <el-button type="text" icon="el-icon-delete" style="font-size:30px;"
                                               :disabled="limit2 || viewIndex.index=='' "
                                               @click="operation='delete'"></el-button>
                                    <span style="font-size: 14px; color:cadetblue">
                                        &nbsp;&nbsp;&nbsp;&nbsp;删除
                                    </span>
                                </p>
                            </el-col>
                            <el-col :span="4" v-show="!limit2">
                                <p style="padding:0;margin:0;">
                                    <el-button type="text" icon="el-icon-user" style="font-size:30px;"
                                               @click="datastyle=7"></el-button>
                                    <span style="font-size: 14px; color:cadetblue">
                                        &nbsp;&nbsp;&nbsp;&nbsp;用户管理
                                    </span>
                                </p>
                            </el-col>
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
                <el-aside width="13%" style="border-right: 2px solid #C0C0C0">
                    <div style="height:40em">
                        <p style="margin:0;line-height:16px;text-align:right;">
                            <span class="list-title">
                                {{showtitle}}
                            </span>
                            <span>
                                <el-button v-show="datastyle && datastyle!=7" type="text"
                                           @click="datastyle=0" icon="el-icon-close"
                                           :class="[datastyle==2 ? 'title2':'title1']"></el-button>
                            </span>
                        </p>
                        <LibraryList v-if="datastyle==4 || datastyle==5" 
                                   :dataStyle="datastyle" 
                                   v-show="datastyle" 
                                   @show-detail="viewIndex=$event"></LibraryList>
                        <LoadLibrary v-if="datastyle==6"
                                     :dataStyle="datastyle"
                                     v-show="datastyle"
                                     @show-detail="viewIndex=$event"></LoadLibrary>
                    </div>
                </el-aside>
                <el-main>
                    <el-row>
                        <el-col :span="20">
                            <div v-show="viewIndex.index">
                                <div v-if="datastyle==4">
                                    <br />
                                </div>
                                <Geom v-if="datastyle==4" 
                                      :geomIndex="getIndex" 
                                      :operation="operation" 
                                      :logClass="getClass"
                                      @resetOperate="operation=$event"></Geom>
                                <MaterDetail :materIndex="viewIndex.index"
                                             v-if="datastyle==5"
                                             :operation="operation" 
                                             :newData="materData" 
                                             @propIndex="propIndex=$event"
                                             @resetOperate="operation=$event"
                                             @materStatus="materStatus=$event"></MaterDetail>
                                <Load :loadIndex="getIndex" 
                                      v-if="datastyle==6" 
                                      :operation="operation" 
                                      :logClass="getClass" 
                                      @resetOperate="operation=$event"></Load>
                            </div>
                            <Users v-if="datastyle==7"
                                   :dataStyle="datastyle"
                                   @close='datastyle=$event'></Users>
                        </el-col>
                        <el-col :span="4" style="border-left: 2px solid #C0C0C0">
                            <div class="show-case" v-show="viewIndex.index">
                                <MaterInput :propIndex="propIndex" @materTemp="materTemp=$event"
                                            v-if="datastyle==5&&logClass==0" :materData="materItem"></MaterInput>
                                <RelativeCase :CaseList="viewIndex.case"
                                              v-if="datastyle==4||datastyle==6"></RelativeCase>
                            </div>
                        </el-col>
                    </el-row>
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style>
    .el-header {
        text-align: center;
        margin-left: 21px;
        margin-right: 21px;
        line-height: 100%;
        float: right;
        padding: 0;
    }

    .el-aside {
        margin-left: 21px;
        text-align: center;
        line-height: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        float: right;
        clear: both;
    }

    .el-main {
        margin-right: 21px;
        text-align: center;
        line-height: 22px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        padding-top: 10px;
    }

    h5 {
        margin-top: 4px;
        margin-bottom: 4px;
    }

    .el-col-4 {
        line-height: 60px;
    }

    .list-title {
        font-size: 14px;
        font-weight: 700;
        text-align: center;
        margin-right: 1em;
    }

    .title1 {
        margin-left: 40px;
        margin-right: 10px
    }

    .title2 {
        margin-left: 10px;
        margin-right: 10px
    }

    .show-case {
        height:430px;
        text-align: center;
        line-height: 10px;
        float: right;
        clear: both;
    }
    .user {
        position: absolute;
        right: 2%;
        top: 1%;
    }
    .user-name{
        font-family:'Times New Roman', Times, serif;
        font-weight:bolder;
    }
</style>

<script>
    import LibraryList from '../components/LibraryList.vue'
    import LoadLibrary from '../components/LoadLibrary.vue'
    import MaterDetail from '../components/MaterDetail.vue'
    import Load from '../components/Load.vue'
    import RelativeCase from '../components/RelativeCase.vue'
    import Geom from '../components/Geom.vue'
    import MaterInput from '../components/MaterInput.vue'
    import Users from '../components/Users.vue'
export default {
    name: 'Dataset',
    inject:['reload'],
    data() {
        return {
            datastyle: 0,
            viewIndex: { index: '', },
            logClass: this.$route.params.logClass,
            logName: this.$route.params.logName,
            limit1: true,
            limit2: true,
            url: require('../../public/R.jpg'),
            operation: 'check',
            propIndex:'Density',
            materTemp:[],
            materData:{
                Density:[{T: '',value:''}],
                CTE:[{T: '',value:''}],
                Capacity:[{T: '',value:''}],
                Conductivity:[{T: '',value:''}],
                Elastic:[{T: '',value:''}],
                Possion:[{T: '',value:''}],
                Yield:[{T: '',value:''}],
                Tangent:[{T: '',value:''}]
            },
            materStatus:-1
        };
    },

    methods: {
        toAnother(tab) {
            if (tab.name == 'first') {
                this.reload;
                this.$router.push({name:'Home', params: { logClass: this.logClass, logName: this.logName }});
            }
        },

        beforeLeaveTab(activeName, oldName) {
            return false
        },
        logoff(){
            this.reload();
            this.$router.push({ name: 'Login' });
        },
        resetMater() {
            this.propIndex = 'Density',
            this.materTemp = [],
            this.materData ={
                Density:[{T: '',value:''}],
                CTE:[{T: '',value:''}],
                Capacity:[{T: '',value:''}],
                Conductivity:[{T: '',value:''}],
                Elastic:[{T: '',value:''}],
                Possion:[{T: '',value:''}],
                Yield:[{T: '',value:''}],
                Tangent:[{T: '',value:''}]
            }
            },
    },

    computed: {
        showtitle() {
            //显示列表标题
            switch (this.datastyle) {
                case 4: return ("结构尺寸库");
                case 5: return ("结构材料库");
                case 6: return ("加载工况库");
            }
        },
        getIndex() {
            return {
                style: this.viewIndex.style,
                index: this.viewIndex.index
            }
        },
        users() {
                if (this.logClass == 1) {
                    return '普通用户'
                } else if (this.logClass == 0) {
                    return '管理员'
                }
        },
        getClass(){
            return this.$route.params.logClass
        },
        materItem(){
            return this.materData[this.propIndex]
        }
    },

    watch: {
        datastyle: {
            handler(newstyle, oldstyle) {
                this.viewIndex = { index: '',};
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
            immediate: true
        },
        materTemp:{
            handler(newdata, olddata) {
                 this.materData[this.materTemp.index] = newdata.data;
            },
        },
        materStatus:{
            handler(newdata, olddata) {
                 this.resetMater();
                 this.materStatus = -1;
            },
        },
        $route(to,from){
            this.logClass = this.$route.params.logClass;
            this.logName = this.$route.params.logName;
        }
    },

    components: {
        LibraryList,
        LoadLibrary,
        MaterDetail,
        Load,
        RelativeCase,
        Geom,
        MaterInput,
        Users
    }
}
</script>
