<template>
    <el-tabs v-model="activeName" >
        <el-tab-pane label="仿真参数" name="first">
            <div>
                <el-tabs :tab-position="tabPosition" style="height: 200px;">
                    <el-tab-pane class="righttab" label="结构参数">
                        <Geom :geomIndex="caseData.SG_ID"></Geom>
                    </el-tab-pane>
                    <el-tab-pane class="righttab" label="结构材料">
                        <Material :materInfor="materInfor"></Material>
                    </el-tab-pane>
                    <el-tab-pane class="righttab" label="加载工况">
                        <Load :loadIndex="loadIndex"></Load>
                    </el-tab-pane>
                </el-tabs>
            </div>
        </el-tab-pane>
        <el-tab-pane label="仿真结果" name="second">
            <Result :resultIndex="index"></Result>
        </el-tab-pane>
    </el-tabs>
</template>

<style>
    .righttab{
        padding-right:0;
    }
</style>

<script>
    import axios from 'axios';
    import Geom from './Geom.vue';
    import Material from './Material.vue';
    import Load from './Load.vue';
    import Result from './Result.vue';
    export default {
        name: 'ViewCase',
        props: { 'index': Object },
        data() {
            return {
                caseData: {},
                activeName: 'first',
                tabPosition: 'right',
                dialogVisible: false,
                materInfor: {},
                loadIndex: {}
            };
        },

        methods: {
            getCase() {
                //获取数据列表
                const path = 'http://localhost:5000/getdata/case';
                axios.get(path)
                    .then((res) => {
                        this.caseData = res.data.case;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求，数据类型由dataStyle控制
                const path = 'http://localhost:5000/getdata/case';
                axios.post(path, payload)
                    .then(() => {
                        this.getCase();
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                        this.getCase()
                    });
            },
        },

        computed: {
            dingGai() {
                if (this.index.style == 1)
                    return ("球形顶盖");
                else if (this.index.style == 2)
                    return ("内带平台球形顶盖");
                else  (this.index.style == 3)
                    return ("平顶盖");
            },
        },

        watch: {
            index: {
                handler(newindex, oldindex) {
                    this.postIndex(newindex);
                },
                deep: true,
            },

            caseData: {
                handler(newindex, oldindex) {
                   this.materInfor = {
                        MHead: newindex.MHead,
                        MHeadAM: newindex.MHeadAM,
                        MRPV: newindex.MRPV,
                        MRPVAM: newindex.MRPVAM,
                        MBolt: newindex.MBolt,
                        MBoltAM: newindex.MBoltAM,
                        MLayer: newindex.MLayer,
                        MLayerAM: newindex.MLayerAM
                    };
                    this.loadIndex = {
                        style: this.index.style,
                        index: newindex.LC_ID
                    };
                },
                deep: true,
            },
        },

        components: {
            Geom,
            Material,
            Load,
            Result,
        }
    };
</script>