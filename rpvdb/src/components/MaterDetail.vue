<template>
    <div>
        <h4 style="margin-top:2em;line-height:1em">{{materIndex}}</h4>
        <el-tabs @tab-click="changeProp">
            <el-tab-pane label="物理性能">
                <el-tabs tab-position="left" @tab-click="getProp1">
                    <el-tab-pane label="密度">
                        <MaterChart :chartData="materData.density" materUnit="Density(g/cm^3)"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="热膨胀系数">
                        <MaterChart :chartData="materData.CTE" materUnit="CTE(×10^-6/℃)"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="比热容">
                        <MaterChart :chartData="materData.capacity" materUnit="Capacity(J/(kg·K))"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="热导率">
                        <MaterChart :chartData="materData.conductivity" materUnit="Conductivity(W/(m·K))"></MaterChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="机械性能">
                <el-tabs tab-position="left" @tab-click="getProp2">
                    <el-tab-pane label=" 弹性模量">
                        <MaterChart :chartData="materData.elastic" materUnit="Elastic(GPa)"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="泊松比">
                        <MaterChart :chartData="materData.possion" materUnit="Possion"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="屈服强度">
                        <MaterChart :chartData="materData.yie" materUnit="Yield(MPa)"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="切线模量">
                        <MaterChart :chartData="materData.tangent" materUnit="Tangent(GPa)"></MaterChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
        </el-tabs>
        <el-dialog  title="新建或修改"
                    :visible.sync="createDialog"
                    width="30%"
                    :close-on-click-modal="closeModal"
                    :showClose="false">
            <p style="color:darkgreen">保持原名进行修改或为新材料命名</p>
            <el-input v-model="newMater" :placeholder="materIndex"></el-input>
            <p style="color:green" v-if="status==1">{{newMater}}新建/修改成功</p>
            <span slot="footer" class="dialog-footer">
                <el-button @click="resetOperation">关闭</el-button>
                <el-button type="primary" @click="createMater">新建/修改</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<style>
</style>

<script>
    import axios from 'axios';
    import MaterChart from './MaterChart.vue';
    export default {
        name: 'MaterDetail',
        props: {'materIndex':String,'newData':Object,'operation':String},
        data() {
            return {
                materData: {},
                propIndex:'Density',
                savedTab:1,
                createDialog: false,
                closeModal:false,
                status:0,
                newMater:this.materIndex
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
                const path = 'http://localhost:5000/getdata/mater';
                axios.get(path)
                    .then((res) => {
                        this.materData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/mater';
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

            options(data) {
                var option = {
                    xAxis: {},
                    yAxis: {},
                    series: [
                        {
                            type: 'line',
                            data: data
                        }
                    ]
                }
                return option
            },

            getProp1(tab){
                this.savedTab = tab.index
                if(tab.index==0) 
                    this.propIndex = 'Density';
                else if(tab.index==1)
                    this.propIndex = 'CTE';
                else if(tab.index==2)
                    this.propIndex = 'Capacity';
                else if(tab.index==3)
                    this.propIndex = 'Conductivity';

            },

            getProp2(tab){
                this.savedTab = tab.index
                if(tab.index==0) 
                    this.propIndex = 'Elastic';
                else if(tab.index==1)
                    this.propIndex = 'Possion';
                else if(tab.index==2)
                    this.propIndex = 'Yield';
                else if(tab.index==3)
                    this.propIndex = 'Tangent';

            },

            changeProp(tab){
                if(tab.index==0){
                    if(this.savedTab==0) 
                        this.propIndex = 'Density';
                    else if(this.savedTab==1)
                        this.propIndex = 'CTE';
                    else if(this.savedTab==2)
                        this.propIndex = 'Capacity';
                    else if(this.savedTab==3)
                        this.propIndex = 'Conductivity';
                }
                else if(tab.index==1){
                    if(this.savedTab==0) 
                        this.propIndex = 'Elastic';
                    else if(this.savedTab==1)
                        this.propIndex = 'Possion';
                    else if(this.savedTab==2)
                        this.propIndex = 'Yield';
                    else if(this.savedTab==3)
                        this.propIndex = 'Tangent';

                }
                
            },

            resetOperation(){
                this.createDialog = false;
                this.status=0;
                this.$emit('resetOperate','check');
            },

            createMater(){
                let mater  = {
                    newMater:this.newMater,
                    newData:this.newData
                }                
                const path = 'http://localhost:5000/create/mater';
                axios.post(path, mater)
                    .then(() => {
                        this.getList('create/mater').then(res => {
                            this.status = res;
                            this.$emit('materStatus',res);
                        })
                    })
            },

            deleteMater() {
                this.$confirm('将永久删除该材料, 是否继续?',{
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    var mater = {
                        index: this.materIndex,
                        style: 5
                    }
                    const path = 'http://localhost:5000/change/delete';
                    axios.post(path, mater)
                        .then(() => {
                            this.$nextTick(() => {
                                this.$emit('resetOperate','check');
                                this.$emit('materStatus',1);
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


        },

        watch: {
            materIndex: {
                handler(newindex, oldindex) {
                    let index = { index: newindex };
                    this.postIndex(index);
                },
                immediate: true,
            },
            propIndex: {
                handler(newindex,oldindex){
                    this.$emit('propIndex',newindex)
                }
            },
            operation:{
                handler(newindex, oldindex) {
                    if(newindex=='create'){
                        this.createDialog = true;
                    }else if(newindex=='check'){
                        this.$emit('resetOperate','check');
                    }else if(newindex=='delete'){
                        this.deleteMater();
                    }
                },
            }
        },

        components: {
            MaterChart,
        }
    };
</script>