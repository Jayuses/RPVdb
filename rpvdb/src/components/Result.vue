<template>
    <div>
        <el-tabs tab-position="right">
            <el-tab-pane label="密封环位置轴向分离量">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultCharts :reData1="resultData.ZX_IN1" 
                                      :reData2="resultData.ZX_OUT1"
                                      reUnit="Value/mm"
                                      process="Time/s"
                                      :series="series1"></ResultCharts>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultCharts :reData1="resultData.ZX_IN2" 
                                      :reData2="resultData.ZX_OUT2"
                                      reUnit="Value/mm"
                                      process="Time/h"
                                      :series="series1"></ResultCharts>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="密封环位置径向分离量">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultCharts :reData1="resultData.JX_IN1" 
                                      :reData2="resultData.JX_OUT1"
                                      reUnit="Value/mm"
                                      process="Time/s"
                                      :series="series1"></ResultCharts>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultCharts :reData1="resultData.JX_IN2" 
                                      :reData2="resultData.JX_OUT2"
                                      reUnit="Value/mm"
                                      process="Time/h"
                                      :series="series1"></ResultCharts>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰相对转角">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultCharts :reData1="resultData.ZJ_U1" 
                                      :reData2="resultData.ZJ_D1"
                                      reUnit="Value/°"
                                      process="Time/s"
                                      :series="series2"></ResultCharts>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultCharts :reData1="resultData.ZJ_U2" 
                                      :reData2="resultData.ZJ_D2"
                                      reUnit="Value/°"
                                      process="Time/h"
                                      :series="series2"></ResultCharts>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰轴向相对位移">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart :reData="resultData.FL_ZKL1"
                                     reUnit="Value/mm"
                                      process="Time/s"></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart :reData="resultData.FL_ZKL2"
                                     reUnit="Value/mm"
                                     process="Time/h"></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰径向相对位移">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart :reData="resultData.FL_JXWYL1"
                                     reUnit="Value/mm"
                                     process="Time/s"></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart :reData="resultData.FL_JXWYL2"
                                     reUnit="Value/mm"
                                     process="Time/h"></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="螺栓应力">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart :reData="resultData.LS_YJL1"
                                     reUnit="Value/MPa"
                                     process="Time/s"></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart :reData="resultData.LS_YJL2"
                                     reUnit="Value/MPa"
                                     process="Time/h"></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<style>
    .re-chart{
        height:100%;
    }
</style>

<script>
    import axios from 'axios';
    import ResultChart from './ResultChart.vue';
    import ResultCharts from './ResultCharts.vue';
    export default {
        name: 'Result',
        //父组件ViewCase传入参数resultIndex{'style':'','index':''}，
        //分别表示顶盖类型与算例名称
        props: {'resultIndex':Object},
        data() {
            return {
                resultData: {},
                series1: ['内环', '外环'],
                series2:['上法兰','下法兰']
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/result';
                axios.get(path)
                    .then((res) => {
                        this.resultData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/result';
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

        watch: {
            resultIndex: {
                handler(newindex, oldindex) {
                    this.postIndex(this.resultIndex);
                },
                deep: true,
                immediate:true
            }
        },

        computed: {
            redatas(data1,data2) {
                return {
                    reData1: data1,
                    reData2: data2,
                }
            }
        },

        components: {
            ResultChart,
            ResultCharts
        }
    };
</script>