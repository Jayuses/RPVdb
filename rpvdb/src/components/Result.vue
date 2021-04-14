<template>
    <div>
        <el-tabs tab-position="right">
            <el-tab-pane label="密封环位置轴向分离量">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart :reData="resultData.result1"></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="密封环位置径向分离量">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰相对转角">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰轴向相对位移">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="法兰径向相对位移">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="螺栓应力">
                <el-tabs tab-position="bottom">
                    <el-tab-pane label="预紧过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                    <el-tab-pane label="服役过程">
                        <ResultChart></ResultChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<style>
    .re-chart{
        height:60%;
    }
</style>

<script>
    import axios from 'axios';
    import ResultChart from './ResultChart.vue';
    export default {
        name: 'Result',
        //父组件ViewCase传入参数resultIndex{'style':'','index':''}，
        //分别表示顶盖类型与算例名称
        props: {'resultIndex':Object},
        data() {
            return {
                resultData: {},
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
            }
        },

        components: {
            ResultChart,
        }
    };
</script>