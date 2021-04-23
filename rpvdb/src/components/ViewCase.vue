<template>
    <div>
        <el-tabs v-model="activeName">
            <el-tab-pane label="仿真参数" name="first">
                <div>
                    <el-tabs :tab-position="tabPosition" style="height: 390px;">
                        <el-tab-pane class="righttab" label="结构参数">
                            <Geom :geomIndex="geomIndex"></Geom>
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
    </div>
</template>

<style>
    .righttab {
        padding-right: 0;
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
                loadIndex: {},
                geomIndex: {}
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

        watch: {
            index: {
                handler(newindex, oldindex) {
                    this.postIndex(newindex);
                },
                deep: true,
                immediate:true,
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
                        MLayerAM: newindex.MLayerAM,
                        style: this.index.style
                    };
                    this.loadIndex = {
                        style: this.index.style,
                        index: newindex.LC_ID
                    };
                    this.geomIndex = {
                        style: this.index.style,
                        index: newindex.SG_ID
                    };
                },
                deep: true,
                immediate: true,
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