<template>
    <div class="the-form">
        <el-steps :active="active" finish-status="success"
                  style="text-align:left;margin-left:10%;margin-right:10%">
            <el-step title="仿真参数"></el-step>
            <el-step title="仿真结果"></el-step>
            <el-step title="案例提交"></el-step>
        </el-steps>
        <div v-if="active==1" class="create-case">
            <p style="color:darkgreen">请从已有库中选择结构、材料、工况，若无请先新建相关库</p>
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
        </div>
        <div class="create-case" v-if="active==2">
            <el-upload class="upload-demo"
                       ref="upload"
                       accept=".xls,.xlsx"
                       action="../assets/temp"
                       :auto-upload="false">
                <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
                <el-button style="margin-left: 10px;" size="small" type="success" >导入</el-button>
                <div slot="tip" class="el-upload__tip">只能上传xls/xlsx文件</div>
            </el-upload>
        </div>
        <div class="create-case" v-if="active==3">
            <p style="color:darkgreen">参考格式：SPSX-XXX-X-XXXX</p>
            <p style="color:darkgreen">其中（自左向右）：SPSX表示顶盖类型；XXX表示案例来源；X表示工况类型；XXXX为自定义编号</p>
            <p style="margin-top: 40px;">
                <span style="margin-right:20px;font-weight:800">
                    案例命名
                </span>
                <span>
                    <el-input v-model="CaseID" placeholder="命名案例"
                              style="width:200px"></el-input>
                </span>
                <span>
                    <el-button @click="create"
                               type="success"
                               size="medium"
                               style="margin-left:30px">案例提交</el-button>
                </span>
                <span>
                    <el-button style="margin-top: 12px;margin-left:40px"
                               @click="resetForm" type="info"
                               size="medium">重置</el-button>
                </span>
            </p>
            <div style="margin-top:20px">
                <p style="color:green" v-if="status==1">{{CaseID}}新建成功</p>
                <p style="color:darkred" v-if="status==2">{{CaseID}}命名重复</p>
                <p style="color:darkred" v-if="status==3">该案例已存在，请直接查取</p>
                <p style="color:darkred" v-if="status==4">请输入/选取{{checkItem}}</p>
            </div>
        </div>
        <p>
            <span>
                <el-button style="margin-top: 12px; "
                           @click="before">上一步</el-button>
            </span>
            <span>
                <el-button style="margin-top: 12px;margin-left:40px"
                           @click="next">下一步</el-button>
            </span>
        </p>      
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
    .create-case{
        height:250px;
        margin-top:30px;
    }
    .upload-demo{
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
                active: 1,
                CaseID: '',
                checkItem:''
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
                this.active = 1;
                this.CaseID = '';
                this.checkItem = '';
            },

            find() {
                //提交表单到后端搜索
                const path = 'http://localhost:5000/search/find';
                axios.post(path, this.caseForm)
                    .then(() => {
                        this.getList('search/find').then(res => {
                            this.caselist = res;
                        })
                    })
            },

            next() {
                if (this.active++ > 2) this.active = 3;
            },
            before() {
                if (this.active-- < 2) this.active = 1;
            },

            create() {
                //新建案例
                var postcase = {
                    CaseID: this.CaseID,
                    caseinfo: this.caseForm
                };
                if (this.checkitem()) {
                    this.status = 4;
                } else {
                    const path = 'http://localhost:5000/search/find';
                    axios.post(path, this.caseForm)
                        .then(() => {
                            this.getList('search/find').then(res => {
                                this.caselist = res;
                                if (this.caselist.length != 0) {
                                    this.status = 3;
                                } else {
                                    const path = 'http://localhost:5000/create/case';
                                    axios.post(path, postcase)
                                        .then(() => {
                                            this.getList('create/case').then(res => {
                                                this.status = res;
                                            })
                                        })
                                }
                            })
                        })
                }
                   
            },

            checkitem() {
                this.checkItem = '';
                if (this.CaseID == '') {
                    this.checkItem = '案例名';
                } else if (this.caseForm.style == '') {
                    this.checkItem = '顶盖类型';
                } else if (this.caseForm.SG_ID == '') {
                    this.checkItem = '尺寸类型';
                } else if (this.caseForm.LC_ID == '') {
                    this.checkItem = '工况类型';
                } else if (this.caseForm.MHead.length == 0) {
                    this.checkItem = '顶盖材料';
                } else if (this.caseForm.MRPV.length == 0) {
                    this.checkItem = '筒体材料';
                } else if (this.caseForm.MBolt.length == 0) {
                    this.checkItem = '螺栓材料';
                } else if (this.caseForm.MLayer.length == 0) {
                    this.checkItem = '堆焊层材料';
                }
                return this.checkItem;
            }
        },

        created() {
            this.getList('search/option').then(res => {
                this.mater = res.mater;
                this.geom = res.geom;
                this.load = res.load;
            })
        }

    }
</script>