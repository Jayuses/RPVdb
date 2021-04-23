<template>
    <div class="the-form">
        <el-steps :active="active" finish-status="success" direction="vertical">
            <el-step title="仿真参数">
                <el-form :inline="true" :model="caseForm" class="demo-form-inline" ref="caseForm">
                    <el-form-item label="顶盖类型">
                        <el-select v-model="caseForm.style" placeholder="顶盖类型" size="mini">
                            <el-option v-for="item in dingGai"
                                       :key="item.value"
                                       :label="item.label"
                                       :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="结构尺寸库">
                        <el-select v-model="caseForm.SG_ID" placeholder="结构尺寸库" size="mini">
                            <el-option v-for="item in geom"
                                       :key="item.value"
                                       :label="item.label"
                                       :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="加载工况库">
                        <el-select v-model="caseForm.LC_ID" placeholder="加载工况库" size="mini">
                            <el-option v-for="item in load"
                                       :key="item.value"
                                       :label="item.label"
                                       :value="item.value">
                            </el-option>
                        </el-select>
                    </el-form-item>
                    <el-form-item label="顶盖材料">
                        <el-cascader v-model="caseForm.MHead"
                                     :options="mater"
                                     size="mini"
                                     placeholder="顶盖材料"></el-cascader>
                    </el-form-item>
                    <el-form-item label="筒体材料">
                        <el-cascader v-model="caseForm.MRPV"
                                     :options="mater"
                                     size="mini"
                                     placeholder="筒体材料"></el-cascader>
                    </el-form-item>
                    <el-form-item label="紧固件材料">
                        <el-cascader v-model="caseForm.MBolt"
                                     :options="mater"
                                     size="mini"
                                     placeholder="紧固件材料"></el-cascader>
                    </el-form-item>
                    <el-form-item label="堆焊层材料">
                        <el-cascader v-model="caseForm.MLayer"
                                     :options="mater"
                                     size="mini"
                                     placeholder="堆焊层材料"></el-cascader>
                    </el-form-item>
                </el-form>
            </el-step>
            <el-step title="仿真结果"></el-step>
            <el-step title="案例提交"></el-step>
        </el-steps>
        <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
    </div>
</template>

<style>
    .the-form {
        line-height: 22px;
    }

    .demo-form-inline {
        margin: 0;
    }

    label.el-form-item__label {
        max-width: 85px;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name:'Search',
        data() {
            return {
                caseForm: {
                    style: [],
                    SG_ID: '',
                    MHead: [],
                    MRPV: [],
                    MBolt: [],
                    MLayer: [],
                    LC_ID:''
                },
                dingGai: [
                    {
                        value: 1,
                        label:'球型顶盖'
                    },
                    {
                        value: 2,
                        label: '内带平台球型顶盖'
                    },
                    {
                        value: 3,
                        label: '平顶盖'
                    },
                ],
                mater: [],
                geom:[],
                load: [],
                caselist: [],
                status: 0,
                active:0
            }
        },

        methods: {
            async getList(url) {
                //获取数据列表
                const path = 'http://localhost:5000/search/' + url;
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

            resetForm() {
                //重置表单
                this.caseForm = {
                    style: [],
                    SG_ID: '',
                    MHead: [],
                    MRPV: [],
                    MBolt: [],
                    MLayer: [],
                    LC_ID: ''
                };
                this.caselist = [];
                this.status = 0;
            },

            find() {
                //提交表单到后端搜索
                const path = 'http://localhost:5000/search/find';
                axios.post(path, this.caseForm)
                    .then(() => {
                        this.getList('find').then(res => {
                            this.caselist = res;
                        })
                        this.status = 1;
                    })
            },
        },

        created() {
            this.getList('option').then(res => {
                this.mater = res.mater;
                this.geom = res.geom;
                this.load = res.load;
            })
        }

    }
</script>