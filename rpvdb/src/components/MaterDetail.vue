<template>
    <div>
        <h4 style="margin:0;line-height:22px">{{materIndex}}</h4>
        <el-tabs>
            <el-tab-pane label="物理性能">
                <el-tabs tab-position="left">
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
                <el-tabs tab-position="left">
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
    </div>
</template>

<style>
</style>

<script>
    import axios from 'axios';
    import MaterChart from './MaterChart.vue';
    export default {
        name: 'MaterDetail',
        props: {'materIndex':String},
        data() {
            return {
                materData: {},
            }
        },

        methods: {
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
            }
        },

        watch: {
            materIndex: {
                handler(newindex, oldindex) {
                    let index = { index: newindex };
                    this.postIndex(index);
                },
                immediate: true,
            },
        },

        components: {
            MaterChart,
        }
    };
</script>