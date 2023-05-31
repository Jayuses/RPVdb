<template>
    <div v-if="loadCon" class="load-infor">
        <br />
        <p class="load-title">
            <span>加载工况库</span>
            <span style="margin-left:30px;" v-if='logClass==0'><input type="text" v-model="loadCon.LT" placeholder="loadCon.LT" style="width:6em"></span>
            <span style="margin-left:30px;">{{loadIndex.index}}</span>
            <span style="margin-left:30px;" v-if='logClass==1'>{{loadCon.LT}}</span>
        </p>
        <table border="1" width="70%" align="center" cellpadding="8" cellspacing="0" class="the-table">
            <tr>
                <th colspan="4">
                    <el-button type="text" @click="dialogVisible1 = true"
                               style="padding:0">温度和内压</el-button>
                </th>
            </tr>
            <tr>
                <th>
                    <el-button type="text" @click="dialogVisible2 = true"
                               style="padding:0">螺栓预紧</el-button>
                </th>
                <td colspan="3" v-if='logClass==0'>预紧力：<input type="number" v-model="loadCon.PreT" placeholder="loadCon.PreT" style="width:6em">&nbsp;N</td>
                <td colspan="3" v-if='logClass==1'>预紧力：{{loadCon.PreT}}&nbsp;N</td>
            </tr>
            <tr>
                <th rowspan="6">
                    <el-button type="text" @click="dialogVisible3 = true"
                               style="padding:0">结构载荷</el-button>
                </th>
                <th rowspan="2">顶盖法兰</th>
                <td v-if='logClass==0'>弹簧回弹力：<input type="number" v-model="loadCon.SR1" placeholder="loadCon.SR1" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==0'>OBE横向载荷: <input type="number" v-model="loadCon.OBET1" placeholder="loadCon.OBET1" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==1'>弹簧回弹力：{{loadCon.SR1}}&nbsp;N</td>
                <td v-if='logClass==1'>OBE横向载荷: {{loadCon.OBET1}}&nbsp;N</td>
            </tr>
            <tr>
                <td colspan="2" v-if='logClass==0'>OBE垂向载荷: <input type="number" v-model="loadCon.OBEA1" placeholder="loadCon.OBEA1" style="width:6em">&nbsp;N</td>
                <td colspan="2" v-if='logClass==1'>OBE垂向载荷:{{loadCon.OBEA1}}&nbsp;N</td>
            </tr>
            <tr>
                <th rowspan="3">筒体法兰</th>
                <td v-if='logClass==0'>构建组件重力：<input type="number" v-model="loadCon.W" placeholder="loadCon.W" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==0'>落棒载荷：<input type="number" v-model="loadCon.CR" placeholder="loadCon.CR" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==1'>构建组件重力：{{loadCon.W}}&nbsp;N</td>
                <td v-if='logClass==1'>落棒载荷：{{loadCon.CR}}&nbsp;N</td>
            </tr>
            <tr>
                <td v-if='logClass==0'>弹簧回弹力：<input type="number" v-model="loadCon.SR2" placeholder="loadCon.SR2" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==0'>OBE横向载荷: <input type="number" v-model="loadCon.OBET2" placeholder="loadCon.OBET2" style="width:6em">&nbsp;N</td>
                <td v-if='logClass==1'>弹簧回弹力：{{loadCon.SR2}}&nbsp;N</td>
                <td v-if='logClass==1'>OBE横向载荷: {{loadCon.OBET2}}&nbsp;N</td>
            </tr>
            <tr>
                <td colspan="2" v-if='logClass==0'>OBE垂向载荷: <input type="number" v-model="loadCon.OBEA2" placeholder="loadCon.OBEA2" style="width:6em">&nbsp;N</td>
                <td colspan="2" v-if='logClass==1'>OBE垂向载荷: {{loadCon.OBEA2}}&nbsp;N</td>
            </tr>
            <tr>
                <th>垫片</th>
                <td v-if='logClass==0'>等效反力：<input type="number" v-model="loadCon.RF" placeholder="loadCon.RF" style="width:6em">&nbsp;MPa</td>
                <td v-if='logClass==0'>等效作用宽度：<input type="number" v-model="loadCon.RW" placeholder="loadCon.RW" style="width:6em">&nbsp;mm</td>
                <td v-if='logClass==1'>等效反力：{{loadCon.RF}}&nbsp;MPa</td>
                <td v-if='logClass==1'>等效作用宽度：{{loadCon.RW}}&nbsp;mm</td>
            </tr>
        </table>
        <el-dialog title="温度与内压"
                   :visible.sync="dialogVisible1"
                   width="50%">
            <el-tabs>
                <el-tab-pane label="加载示意图">
                    <el-image :src="url4"></el-image>
                </el-tab-pane>
                <el-tab-pane label="T(P)-t图">
                    <TP :tpData="tpdata"></TP>
                </el-tab-pane>
            </el-tabs>
        </el-dialog>
        <el-dialog title="螺栓预紧"
                   :visible.sync="dialogVisible2"
                   width="50%">
            <el-image :src="url1"></el-image>
        </el-dialog>
        <el-dialog title="结构载荷"
                   :visible.sync="dialogVisible3"
                   width="80%">
            <table>
                <tr>
                    <td><el-image :src="url2"></el-image></td>
                    <td><el-image :src="url3"></el-image></td>
                </tr>
            </table>
        </el-dialog>
        <el-dialog  title="新建或修改"
                    :visible.sync="createDialog"
                    width="40%"
                    :close-on-click-modal="false"
                    :showClose="false">
            <p style="color:darkgreen">保持原名进行修改或为新结构尺寸命名</p>
            <el-input v-model="loadCon.LC_ID" placeholder="loadCon.LC_ID"></el-input>
            <div>
                <p style="color:darkgreen">温度和内压</p>
                <el-table :data="newTP" style="width: 100%" max-height="250" >
                    <el-table-column prop="time" label="时间">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.time" placeholder="请输入"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column prop="T" label="温度">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.T" placeholder="请输入"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column prop="p" label="压力">
                        <template slot-scope="scope">
                            <el-input v-model="scope.row.p" placeholder="请输入"></el-input>
                        </template>
                    </el-table-column>
                    <el-table-column label="操作" width="70%">
                        <template slot-scope="scope">
                            <div style="display: flex;justify-content: space-between;">
                                <el-link icon="el-icon-plus" size="mini" type="primary"
                                    @click="handleAdd(scope.$index, scope.row)" :underline="false"></el-link>
                                <el-link icon="el-icon-delete" size="mini" @click="handleDelete(scope.$index, scope.row)"
                                    type="danger" :underline="false"></el-link>
                            </div>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
            <p style="color:green" v-if="status==1">{{loadCon.LC_ID}}新建/修改成功</p>
            <span slot="footer" class="dialog-footer">
                
                <el-button @click="resetOperation">关闭</el-button>
                <el-button type="primary" @click="createLoad">新建/修改</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<style>
    .load-title {
        text-align: center;
        margin: 10px;
        font-size: 16px;
        /*border-bottom: 2px solid #C0C0C0;*/
    }
    .the-table{
        margin-top:4%
    }
    .load-infor {
        margin-top: 3em;
    }
</style>

<script>
    import axios from 'axios';
    import TP from './TP.vue';
    export default {
        name: 'Geom',
        props: { 'loadIndex': Object, 'operation': String, 'logClass': Number},
        data() {
            return {
                loadCon: {},
                loadT:{},
                loadP:{},
                dialogVisible1: false,
                dialogVisible2: false,
                dialogVisible3: false,
                createDialog:false,
                status:0,
                test:0,
                newTP:[{
                    time: '',
                    T: '',
                    p: ''
                }]
            }
        },

        methods: {
            async getList(url) {
                //获取数据列表
                const path = 'http://localhost:5000/' + url;
                let options = [];
                await axios.get(path)
                    .then((res) => {
                        options = res.data;
                    })
                /*.catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });*/
                return options;
            },
            getData() {
                const path = 'http://localhost:5000/getdata/load';
                axios.get(path)
                    .then((res) => {
                        this.test = 2;
                        this.loadCon = res.data.loadCon;
                        this.loadT = res.data.loadT;
                        this.loadP = res.data.loadP;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },
            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/load';
                axios.post(path, payload)
                    .then(() => {
                        this.test = 1;
                        this.getData();
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                        this.getData();
                    });
            },
            resetOperation(){
                this.createDialog = false;
                this.deleteDialog = false
                this.status=0;
                this.$emit('resetOperate','check');
            },
            createLoad(){
                var Load = {
                    newCon:this.loadCon,
                    newTP:this.newTP,
                    style:this.loadIndex.style
                }                
                const path = 'http://localhost:5000/create/load';
                axios.post(path, Load)
                    .then(() => {
                        this.getList('create/load').then(res => {
                            this.status = res;
                        })
                    })
            },
            deleteload() {
                this.$confirm('将永久删除该加载工况及相关案例, 是否继续?',{
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    var load = {
                        index: this.loadIndex.index,
                        style: 6
                    }
                    const path = 'http://localhost:5000/change/delete';
                    axios.post(path, load)
                        .then(() => {
                            this.$nextTick(() => {
                                this.$emit('resetOperate','check');
                            })
                        })
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });
                }).catch(() => {
                    this.$emit('resetOperate','check');
                });
                
            },
            handleAdd(index, row) {
                this.newTP.push({
                    time: '',
                    T: '',
                    p: ''
                });
            },
            handleDelete(index,row) {
                if (index > 0) {
                    this.newTP.splice(index, 1);
                }
            },
        },

        computed: {
            url1() {
                if (this.loadIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖-预紧单元.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-螺栓预紧单元.png')
                else 
                    return require('../assets/image/path3/平顶盖-螺栓预紧单元.png')
            },
            url2() {
                if (this.loadIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖-机械载荷.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-机械载荷.png')
                else
                    return require('../assets/image/path3/平顶盖-机械载荷.png')
            },
            url3() {
                if (this.loadIndex.style == 1 )
                    return require('../assets/image/path1/球形顶盖-垫片反力.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-垫片反力.png')
                else
                    return require('../assets/image/path3/平顶盖-垫片反力.png')
            },
            url4() {
                if (this.loadIndex.style == 1 )
                    return require('../assets/image/path1/球形顶盖-温度加载示意图.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-温度加载示意图.png')
                else
                    return require('../assets/image/path3/平顶盖-温度加载示意图.png')
            },

            tpdata() {
                return {
                    tData: this.loadT,
                    pData: this.loadP
                }
            }
        },

        watch: {
            loadIndex: {
                handler(newindex,_) {
                    this.postIndex(newindex);
                },
                deep: true,
                immediate:true
            },
            operation:{
                handler(newindex,_) {
                    if(newindex=='create'){
                        this.createDialog = true;
                    }else if(newindex=='check'){
                        this.$emit('resetOperate','check');
                    }else if(newindex=='delete'){
                        this.deleteload();
                    }
                },
            }
        },

        components:{
            TP
        }
    };
</script>