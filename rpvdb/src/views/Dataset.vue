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
                                            <el-button type="text" @click="datastyle=4"> 结构尺寸库 </el-button>
                                        </el-col>
                                        <el-col :span="6">
                                            <el-button type="text" @click="datastyle=5"> 结构材料库 </el-button>
                                        </el-col>
                                        <el-col :span="6">
                                            <el-button type="text" @click="datastyle=6"> 加载工况库 </el-button>
                                        </el-col>
                                    </el-row>
                                </span>
                            </el-col>
                            <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                <p style="padding:0;margin:0;">
                                    <el-button type="text" icon="el-icon-plus" style="font-size:30px;"></el-button>
                                    <span style="font-size: 14px; color:cadetblue">
                                        &nbsp;&nbsp;&nbsp;&nbsp;新建
                                    </span>
                                </p>
                            </el-col>
                            <el-col :span="4" style="border-right: 1px solid #C0C0C0">
                                <p style="padding:0;margin:0;">
                                    <el-button type="text" icon="el-icon-delete" style="font-size:30px;"></el-button>
                                    <span style="font-size: 14px; color:cadetblue">
                                        &nbsp;&nbsp;&nbsp;&nbsp;删除
                                    </span>
                                </p>
                            </el-col>
                        </el-tab-pane>
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
                            <div style="height:400px" v-show="viewIndex.index">
                                <div v-if="datastyle==4">
                                    <br />
                                </div>
                                <Geom :geomIndex="getIndex" v-if="datastyle==4"></Geom>
                                <MaterDetail :materIndex="viewIndex.index" v-if="datastyle==5"></MaterDetail>
                                <Load :loadIndex="getIndex" v-if="datastyle==6"></Load>
                            </div>
                        </el-col>
                        <el-col :span="4" style="border-left: 2px solid #C0C0C0">
                            <div class="show-case" v-show="viewIndex.index">
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
</style>

<script>
    import LibraryList from '../components/LibraryList.vue'
    import LoadLibrary from '../components/LoadLibrary.vue'
    import MaterDetail from '../components/MaterDetail.vue'
    import Load from '../components/Load.vue'
    import RelativeCase from '../components/RelativeCase.vue'
    import Geom from '../components/Geom.vue'
export default {
    name: 'Dataset',
    data() {
        return {
            datastyle: 0,
            viewIndex: { index: '',}
        };
    },

    methods: {
        toAnother(tab) {
            if (tab.name == 'first') {
                this.$router.push('/home');
            }
        },

        beforeLeaveTab(activeName, oldName) {
            return false
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
        }    
    },

    watch: {
        datastyle: {
            handler(newstyle, oldstyle) {
                this.viewIndex = { index: '',}
            }
        },
    },

    components: {
        LibraryList,
        LoadLibrary,
        MaterDetail,
        Load,
        RelativeCase,
        Geom
    }
}
</script>
