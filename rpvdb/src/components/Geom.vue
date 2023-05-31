<template>
    <div>
        <p class="gemo-title">
            <span>
                <el-button type="text" @click="dialogVisible = true">{{dingGai}}密封</el-button>
                <el-dialog :title="dingGai"
                           :visible.sync="dialogVisible"
                           width="30%">
                    <el-image :src="dingGai_url"></el-image>
                </el-dialog>
            </span>
            <span style="margin-left:7%;">结构参数库</span>
            <span style="margin-left:10%;">{{geomIndex.index}}</span>
        </p>
        <el-row>
            <el-col :span="10">
                <div class="p-para">
                    <el-tabs tab-position="bottom" class="p-para">
                        <el-tab-pane label="顶盖" >
                            <div class="tab-content" v-if="logClass==1">
                                <p>D1 = {{geomData.D1}} mm</p>
                                <p>D2 = {{geomData.D2}} mm</p>
                                <p>D3 = {{geomData.D3}} mm</p>
                                <p>D4 = {{geomData.D4}} mm</p>
                                <p>D5 = {{geomData.D5}} mm</p>
                                <p>D6 = {{geomData.D6}} mm</p>
                                <p>R1 = {{geomData.R1}} mm</p>
                                <p>SR2 = {{geomData.SR2}} mm</p>
                                <p>R3 = {{geomData.R3}} mm</p>
                                <p>h1 = {{geomData.h1}} mm</p>
                                <p>h2 = {{geomData.h2}} mm</p>
                                <p>t1 = {{geomData.t1}} mm</p>
                                <p>m = {{geomData.m}} (螺栓个数)</p>
                                <p>n = {{geomData.n}} (螺栓个数)</p>
                            </div>
                            <div class="tab-content" v-if="logClass==0">
                                <p>D1 = <input type="number" v-model="geomData.D1" placeholder="geomData.D1" style="width:6em"> mm</p>
                                <p>D2 = <input type="number" v-model="geomData.D2" placeholder="geomData.D2" style="width:6em"> mm</p>
                                <p>D3 = <input type="number" v-model="geomData.D3" placeholder="geomData.D3" style="width:6em"> mm</p>
                                <p>D4 = <input type="number" v-model="geomData.D4" placeholder="geomData.D4" style="width:6em"> mm</p>
                                <p>D5 = <input type="number" v-model="geomData.D5" placeholder="geomData.D5" style="width:6em"> mm</p>
                                <p>D6 = <input type="number" v-model="geomData.D6" placeholder="geomData.D6" style="width:6em"> mm</p>
                                <p>R1 = <input type="number" v-model="geomData.R1" placeholder="geomData.R1" style="width:6em"> mm</p>
                                <p>SR2 = <input type="number" v-model="geomData.SR2" placeholder="geomData.SR2" style="width:6em"> mm</p>
                                <p>R3 = <input type="number" v-model="geomData.R3" placeholder="geomData.R3" style="width:6em"> mm</p>
                                <p>h1 = <input type="number" v-model="geomData.h1" placeholder="geomData.h1" style="width:6em"> mm</p>
                                <p>h2 = <input type="number" v-model="geomData.h2" placeholder="geomData.h2" style="width:6em"> mm</p>
                                <p>t1 = <input type="number" v-model="geomData.t1" placeholder="geomData.t1" style="width:6em"> mm</p>
                                <p>m = <input type="number" v-model="geomData.m" placeholder="geomData.m" style="width:6em"> (螺栓个数)</p>
                                <p>n = <input type="number" v-model="geomData.n" placeholder="geomData.n" style="width:6em"> (螺栓个数)</p>
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="筒体">
                            <div class="tab-content" v-if="logClass==1">
                                <p>D7 = {{geomData.D7}} mm</p>
                                <p>D8 = {{geomData.D8}} mm</p>
                                <p>D9 = {{geomData.D9}} mm</p>
                                <p>D10 = {{geomData.D10}} mm</p>
                                <p>h3 = {{geomData.h3}} mm</p>
                                <p>h4 = {{geomData.h4}} mm</p>
                                <p>h5 = {{geomData.h5}} mm</p>
                                <p>R4 = {{geomData.R4}} mm</p>
                                <p>θ = {{geomData.θ}} &deg;</p>
                                <p>t2 = {{geomData.t2}} mm</p>
                            </div>
                            <div class="tab-content" v-if="logClass==0">
                                <p>D7 = <input type="number" v-model="geomData.D7" placeholder="geomData.D7" style="width:6em"> mm</p>
                                <p>D8 = <input type="number" v-model="geomData.D8" placeholder="geomData.D8" style="width:6em"> mm</p>
                                <p>D9 = <input type="numbert" v-model="geomData.D9" placeholder="geomData.D9" style="width:6em"> mm</p>
                                <p>D10 = <input type="number" v-model="geomData.D10" placeholder="geomData.D10" style="width:6em"> mm</p>
                                <p>h3 = <input type="numbert" v-model="geomData.h3" placeholder="geomData.h3" style="width:6em"> mm</p>
                                <p>h4 = <input type="number" v-model="geomData.h4" placeholder="geomData.h4" style="width:6em"> mm</p>
                                <p>h5 = <input type="number" v-model="geomData.h5" placeholder="geomData.h5" style="width:6em"> mm</p>
                                <p>R4 = <input type="number" v-model="geomData.R4" placeholder="geomData.R4" style="width:6em"> mm</p>
                                <p>θ = <input type="number" v-model="geomData.θ" placeholder="geomData.θ" style="width:6em"> &deg;</p>
                                <p>t2 = <input type="number" v-model="geomData.t2" placeholder="geomData.t2" style="width:6em"> mm</p>
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="密封面">
                            <div class="tab-content" v-if="logClass==1">
                                <p>D11 = {{geomData.D11}} mm</p>
                                <p>D12 = {{geomData.D12}} mm</p>
                                <p>D13 = {{geomData.D13}} mm</p>
                                <p>D14 = {{geomData.D14}} mm</p>
                                <p>D15 = {{geomData.D15}} mm</p>
                                <p>D16 = {{geomData.D16}} mm</p>
                                <p>D17 = {{geomData.D17}} mm</p>
                                <p>h6 = {{geomData.h6}} mm</p>
                                <p>L1 = {{geomData.L1}} mm</p>
                                <p>L2 = {{geomData.L2}} mm</p>
                            </div>
                            <div class="tab-content" v-if="logClass==0">
                                <p>D11 = <input type="number" v-model="geomData.D11" placeholder="geomData.D11" style="width:6em"> mm</p>
                                <p>D12 = <input type="number" v-model="geomData.D12" placeholder="geomData.D12" style="width:6em"> mm</p>
                                <p>D13 = <input type="number" v-model="geomData.D13" placeholder="geomData.D13" style="width:6em"> mm</p>
                                <p>D14 = <input type="number" v-model="geomData.D14" placeholder="geomData.D14" style="width:6em"> mm</p>
                                <p>D15 = <input type="number" v-model="geomData.D15" placeholder="geomData.D15" style="width:6em"> mm</p>
                                <p>D16 = <input type="number" v-model="geomData.D16" placeholder="geomData.D16" style="width:6em"> mm</p>
                                <p>D17 = <input type="number" v-model="geomData.D17" placeholder="geomData.D17" style="width:6em"> mm</p>
                                <p>h6 = <input type="number" v-model="geomData.h6" placeholder="geomData.h6" style="width:6em"> mm</p>
                                <p>L1 = <input type="number" v-model="geomData.L1" placeholder="geomData.L1" style="width:6em"> mm</p>
                                <p>L2 = <input type="number" v-model="geomData.L2" placeholder="geomData.L2" style="width:6em"> mm</p>
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="螺栓连接">
                            <div class="tab-content" v-if="logClass==1">
                                <p>D18 = {{geomData.D18}} mm</p>
                                <p>D19 = {{geomData.D19}} mm</p>
                                <p>h7 = {{geomData.h7}} mm</p>
                                <p>h8 = {{geomData.h8}} mm</p>
                            </div>
                            <div class="tab-content" v-if="logClass==0">
                                <p>D18 = <input type="number" v-model="geomData.D18" placeholder="geomData.D18" style="width:6em"> mm</p>
                                <p>D19 = <input type="number" v-model="geomData.D19" placeholder="geomData.D19" style="width:6em"> mm</p>
                                <p>h7 = <input type="number" v-model="geomData.h7" placeholder="geomData.h7" style="width:6em"> mm</p>
                                <p>h8 = <input type="number" v-model="geomData.h8" placeholder="geomData.h8" style="width:6em"> mm</p>
                            </div>
                        </el-tab-pane>
                    </el-tabs>
                </div>
            </el-col>
            <el-col :span="14">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="整体结构">
                        <el-image :src="struc_url1" class="tab-pic"></el-image>
                    </el-tab-pane>
                    <el-tab-pane label="密封结构">
                        <el-image :src="struc_url2" class="tab-pic"></el-image>
                    </el-tab-pane>
                </el-tabs>
            </el-col>
        </el-row>
        <el-dialog  title="新建或修改"
                    :visible.sync="createDialog"
                    width="30%"
                    :close-on-click-modal="closeModal"
                    :showClose="false">
            <p style="color:darkgreen">保持原名进行修改或为新结构尺寸命名</p>
            <el-input v-model="geomData.SG_ID" placeholder="geomData.SG_ID"></el-input>
            <p style="color:green" v-if="status==1">{{CaseID}}新建/修改成功</p>
            <span slot="footer" class="dialog-footer">
                <el-button @click="resetOperation">关闭</el-button>
                <el-button type="primary" @click="createGeom">新建/修改</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<style>
    .el-dialog__header{
        padding:20px;
        font-weight:700;
        text-align:center;
    }
    .el-dialog__body{
        padding-top:0;
    }
    .gemo-title {
        text-align: left;
        margin: 0;
        font-size: 14px;
        border-bottom: 2px solid #F0F0F0;
    }
    .struc-para {
        border: 1px solid #C0C0C0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        font-size: 14px;
    }
    .p-para p {
        margin: 0;
        padding: 4px;
        text-align: center;
        font-size: 14px;
        line-height:10px;
    }
    .struc-pic{
        padding:0;
    }
    .struc-image {
        height: 30em;
    }
    .tab-content {
        height: 28em;
        padding-left:100px;
        display: table-cell;
        vertical-align: middle;
    }
    .tab-pic {
        height: 27em;
        padding-top:2%;
        display: table-cell;
        vertical-align: middle;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'Geom',
        props: { 'geomIndex': Object, 'operation': String, 'logClass': Number },
        data() {
            return {
                geomData: {},
                dialogVisible: false,
                createDialog: false,
                closeModal:false,
                status:0
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
                //获取结构参数
                const path = 'http://localhost:5000/getdata/geom';
                axios.get(path)
                    .then((res) => {
                        this.geomData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/geom';
                axios.post(path, payload)
                    .then(() => {
                        this.getData();
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                        this.getData();
                    });
            },

            createGeom(){
                var geom = {
                    newGeom:this.geomData,
                    style:this.geomIndex.style
                }                
                const path = 'http://localhost:5000/create/geom';
                axios.post(path, geom)
                    .then(() => {
                        this.getList('create/geom').then(res => {
                            this.status = res;
                        })
                    })
            },

            deleteGeom() {
                this.$confirm('将永久删除该结构尺寸及相关案例, 是否继续?',{
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    var geom = {
                        index: this.geomData.SG_ID,
                        style: 4
                    }
                    const path = 'http://localhost:5000/change/delete';
                    axios.post(path, geom)
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

            resetOperation(){
                this.createDialog = false;
                this.status=0;
                this.$emit('resetOperate','check');
            }
        },

        computed: {
            dingGai() {
                let str = ''
                if (this.geomIndex.style == 1)
                    str = "球形顶盖";
                else if (this.geomIndex.style == 2)
                    str = "内带平台球形顶盖";
                else if (this.geomIndex.style == 3)
                    str = "平顶盖";
                return str;
            },
            dingGai_url() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_密封结构_3D.jpg');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_密封结构_3D.png');
                else 
                    return require('../assets/image/path3/平顶盖-密封结构_3D.png');
            },
            struc_url1() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_整体结构图.png');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_整体结构图.png');
                else 
                    return require('../assets/image/path3/平顶盖-整体结构.png');
            },
            struc_url2() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_密封结构图.png');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_整体结构图.png');
                else 
                    return require('../assets/image/path3/平顶盖-整体结构.png');
            },
        },
        
        watch: {
            geomIndex: {
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
                        this.deleteGeom();
                    }
                },
            }
        },
    };
</script>