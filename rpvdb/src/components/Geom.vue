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
            <span style="margin-left:30px;">结构参数库</span>
            <span style="margin-left:30px;">{{geomIndex.index}}</span>
        </p>
        <el-row>
            <el-col :span="10">
                <div class="p-para">
                    <el-tabs type="border-card" class="p-para">
                        <el-tab-pane label="顶盖" >
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
                        </el-tab-pane>
                        <el-tab-pane label="筒体">
                            <p>D7 = {{geomData.D7}} mm</p>
                            <p>D8 = {{geomData.D8}} mm</p>
                            <p>D9 = {{geomData.D9}} mm</p>
                            <p>D10 = {{geomData.D10}} mm</p>
                            <p>h3 = {{geomData.h3}} mm</p>
                            <p>h4 = {{geomData.h4}} mm</p>
                            <p>h5 = {{geomData.h5}} mm</p>
                            <p>R4 = {{geomData.R4}} mm</p>
                            <p>&#952 = {{geomData.θ}} &deg;</p>
                            <p>t2 = {{geomData.t2}} mm</p>
                        </el-tab-pane>
                        <el-tab-pane label="密封面">
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
                        </el-tab-pane>
                        <el-tab-pane label="螺栓连接">
                            <p>D18 = {{geomData.D18}} mm</p>
                            <p>D19 = {{geomData.D19}} mm</p>
                            <p>h7 = {{geomData.h7}} mm</p>
                            <p>h8 = {{geomData.h8}} mm</p>
                        </el-tab-pane>
                    </el-tabs>
                </div>
            </el-col>
            <el-col :span="14">
                <el-tabs type="border-card" class="struct-taps">
                    <el-tab-pane label="整体结构">
                        <el-image :src="struc_url1" ></el-image>
                    </el-tab-pane>
                    <el-tab-pane label="密封结构">
                        <el-image :src="struc_url2"  ></el-image>
                    </el-tab-pane>
                </el-tabs>
            </el-col>
        </el-row>
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
        text-align:left;
        margin: 0;
        font-size: 14px;
        /*border-bottom: 2px solid #C0C0C0;*/
    }
    .struc-para {
        border: 1px solid #C0C0C0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        font-size: 14px;
    }
    .p-para {
        height: 310px;
    }
    .p-para p {
        margin: 0;
        padding: 4px;
        text-align: center;
        font-size: 14px;
    }
    .struct-taps {
        height: 310px;
    }
    .struc-pic{
        padding:0;
    }
    .struc-image {
        height: 280px;
    }

</style>

<script>
    import axios from 'axios';
    export default {
        name: 'Geom',
        props: { 'geomIndex': Object },
        data() {
            return {
                geomData: {},
                dialogVisible: false,
            }
        },

        methods: {
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
        },

        computed: {
            dingGai() {
                if (this.geomIndex.style == 1)
                    return ("球形顶盖");
                else if (this.geomIndex.style == 2)
                    return ("内带平台球形顶盖");
                else if (this.geomIndex.style == 3)
                    return ("平顶盖");
            },
            dingGai_url() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_密封结构_3D.jpg');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_密封结构_3D.png');
                else if (this.geomIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-密封结构_3D.png');
            },
            struc_url1() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_整体结构图.png');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_整体结构图.png');
                else if (this.geomIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-整体结构.png');
            },
            struc_url2() {
                if (this.geomIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖_密封结构图.png');
                else if (this.geomIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_整体结构图.png');
                else if (this.geomIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-整体结构.png');
            }
        },
        
        watch: {
            geomIndex: {
                handler(newindex, oldindex) {
                    this.postIndex(newindex);
                },
                deep: true,
            }
        },
    };
</script>