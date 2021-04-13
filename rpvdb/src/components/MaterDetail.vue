<template>
    <div>
        <h4 style="margin:0">{{materIndex}}</h4>
        <p>{{materData}}</p>
        <el-tabs>
            <el-tab-pane label="物理性能">
                <el-tabs tab-position="left">
                    <el-tab-pane label="密度">
                       <MaterChart :chartData="materData.density"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="热膨胀系数">
                        <MaterChart :chartData="materData.CTE"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="比热容">
                        <MaterChart :chartData="materData.capacity"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="热导率">
                        <MaterChart :chartData="materData.conductivity"></MaterChart>
                    </el-tab-pane>
                </el-tabs>
            </el-tab-pane>
            <el-tab-pane label="机械性能">
                <el-tabs tab-position="left">
                    <el-tab-pane label="弹性模量">
                        <MaterChart :chartData="materData.elastic"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="泊松比">
                        <MaterChart :chartData="materData.possion"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="屈服强度">
                        <MaterChart :chartData="materData.yie"></MaterChart>
                    </el-tab-pane>
                    <el-tab-pane label="切线模量">
                        <MaterChart :chartData="materData.tangent"></MaterChart>
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
    import hello from './hello.vue';
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
        },

        watch: {
            materIndex: {
                handler(newindex, oldindex) {
                    let index = { index: newindex };
                    this.postIndex(index);
                },
                immediate: true,
            }
        },

        components: {
            MaterChart,
            hello
        }
    };
</script>