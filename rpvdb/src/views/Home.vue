<template>
    <div class="home">
        <el-container style="height:100%">
            <el-header>
                <div>
                    <el-tabs type="border-card" value="first">
                        <el-tab-pane label="查看" name="first">
                            <el-row :gutter="20">
                                <el-col :span="11" style="border-right: 3px solid #C0C0C0">
                                    <h5>查看算例</h5>
                                    <span>
                                        <el-row>
                                            <el-col :span="6" :offset="3">
                                                <el-button type="text" @click="datastyle=1"> 球形顶盖 </el-button>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-button type="text" @click="datastyle=2"> 内带平台球形顶盖 </el-button>
                                            </el-col>
                                            <el-col :span="6">
                                                <el-button type="text" @click="datastyle=3"> 平顶盖 </el-button>
                                            </el-col>
                                        </el-row>
                                    </span>
                                </el-col>
                                <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                    <!--<h5>结构尺寸</h5>-->
                                    <span>
                                        <el-button type="text" @click="datastyle=4"> 结构尺寸库 </el-button>
                                    </span>
                                </el-col>
                                <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                    <!--<h5>结构材料</h5>-->
                                    <span>
                                        <el-button type="text" @click="datastyle=7"> 结构材料库 </el-button>
                                    </span>
                                </el-col>
                                <el-col :span="4">
                                    <!--<h5>加载工况</h5>-->
                                    <span>
                                        <el-button type="text" @click="datastyle=8"> 加载工况库 </el-button>
                                    </span>
                                </el-col>
                            </el-row>
                        </el-tab-pane>
                        <el-tab-pane label="输入" name="second">输入数据</el-tab-pane>
                    </el-tabs>
                </div>
            </el-header>
            <br /><br /><br /><br />
            <el-container>
                <el-aside width="200px" style="border-right: 2px solid #C0C0C0">
                    <div style="height:470px">
                        <p style="margin:0;line-height:16px;text-align:right">
                            <span class="list-title">
                                {{showtitle}}
                            </span>
                            <span>
                                <el-button v-show="datastyle" type="text"
                                           @click="datastyle=0" icon="el-icon-close"
                                           style="margin-left:50px"></el-button>
                            </span>
                        </p>
                        <ViewAside :dataStyle="datastyle" v-show="datastyle" @show-detail="viewIndex=$event"></ViewAside>
                    </div>
                </el-aside>
                <el-main>
                    <ViewCase :index="viewIndex" style="line-height:10px"
                              v-show="datastyle"></ViewCase>
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
</style>

<script>
import ViewAside from '../components/ViewAside.vue'
import ViewCase from '../components/ViewCase.vue'
export default {
    name: 'Home',
    data() {
        return {
            datastyle: 0,
            viewIndex: {
                style: this.datastyle,
                index:''
            }
        };
    },

    methods: {
        
    },

    computed: {
        showtitle() {
         //显示列表标题
            switch (this.datastyle) {
                case 1: return ("球形顶盖");
                case 2: return ("内带平台球形顶盖");
                case 3: return ("平顶盖");
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
        }
    },

    components: {
        ViewAside,
        ViewCase,
    }
}
</script>
