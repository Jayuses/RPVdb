<template>
    <div v-if="loadData.loadCon">
        <br />
        <p class="load-title">
            <span>加载工况库</span>
            <span style="margin-left:30px;" >{{loadIndex.index}}</span>
            <span style="margin-left:30px;" >{{loadData.loadCon.LT}}</span>
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
                <td colspan="3">预紧力：{{loadData.loadCon.PreT}}&nbsp;N</td>
            </tr>
            <tr>
                <th rowspan="6">
                    <el-button type="text" @click="dialogVisible3 = true"
                               style="padding:0">结构载荷</el-button>
                </th>
                <th rowspan="2">顶盖法兰</th>
                <td>弹簧回弹力：{{loadData.loadCon.SR1}}&nbsp;N</td>
                <td>OBE横向载荷：{{loadData.loadCon.OBET1}}&nbsp;N</td>
            </tr>
            <tr>
                <td colspan="2">OBE垂向载荷：{{loadData.loadCon.OBEA1}}&nbsp;N</td>
            </tr>
            <tr>
                <th rowspan="3">筒体法兰</th>
                <td>构建组件重力：{{loadData.loadCon.W}}&nbsp;N</td>
                <td>落棒载荷：{{loadData.loadCon.CR}}&nbsp;N</td>
            </tr>
            <tr>
                <td>弹簧回弹力：{{loadData.loadCon.SR2}}&nbsp;N</td>
                <td>OBE横向载荷：{{loadData.loadCon.OBET2}}&nbsp;N</td>
            </tr>
            <tr>
                <td colspan="2">OBE垂向载荷：{{loadData.loadCon.OBEA2}}&nbsp;N</td>
            </tr>
            <tr>
                <th>垫片</th>
                <td>等效反力：{{loadData.loadCon.RF}}&nbsp;MPa</td>
                <td>等效作用宽度：{{loadData.loadCon.RW}}&nbsp;mm</td>
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
</style>

<script>
    import axios from 'axios';
    import TP from './TP.vue';
    export default {
        name: 'Geom',
        props: { 'loadIndex': Object },
        data() {
            return {
                loadData: {},
                dialogVisible1: false,
                dialogVisible2: false,
                dialogVisible3: false,
                test : 0
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/load';
                axios.get(path)
                    .then((res) => {
                        this.test = 2;
                        this.loadData = res.data;
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
        },

        computed: {
            url1() {
                if (this.loadIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖-预紧单元.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-螺栓预紧单元.png')
                else if (this.loadIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-螺栓预紧单元.png')
            },
            url2() {
                if (this.loadIndex.style == 1)
                    return require('../assets/image/path1/球形顶盖-机械载荷.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-机械载荷.png')
                else if (this.loadIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-机械载荷.png')
            },
            url3() {
                if (this.loadIndex.style == 1 )
                    return require('../assets/image/path1/球形顶盖-垫片反力.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-垫片反力.png')
                else if (this.loadIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-垫片反力.png')
            },
            url4() {
                if (this.loadIndex.style == 1 )
                    return require('../assets/image/path1/球形顶盖-温度加载示意图.png')
                else if (this.loadIndex.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖-温度加载示意图.png')
                else if (this.loadIndex.style == 3)
                    return require('../assets/image/path3/平顶盖-温度加载示意图.png')
            },

            tpdata() {
                return {
                    tData: this.loadData.loadT,
                    pData: this.loadData.loadP
                }
            }
        },

        watch: {
            loadIndex: {
                handler(newindex, oldindex) {
                    this.postIndex(newindex);
                },
                deep: true,
                immediate:true
            }
        },

        components:{
            TP
        }
    };
</script>