<template>
    <div ref="main" style="width: 600px;height:330px;"></div>
</template>

<script>
    // 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
    import * as echarts from 'echarts/core';
    // 引入折线图，散点图图表，图表后缀都为 Chart
    import {
        LineChart,
        ScatterChart,
    } from 'echarts/charts';
    // 引入提示框，标题，直角坐标系组件，组件后缀都为 Component
    import {
        TitleComponent,
        TooltipComponent,
        GridComponent,
    } from 'echarts/components';
    // 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
    import {
        CanvasRenderer
    } from 'echarts/renderers';
    //注册必须的组件
    echarts.use(
        [TitleComponent, TooltipComponent, GridComponent, LineChart, ScatterChart, CanvasRenderer]
    );
    export default {
        name: 'ResultCharts',
        props: {'reData1':Array,'reData2':Array},
        data() {
            return {
                option: {
                    grid: {
                        top: '5%',
                        left: '15%',
                        bottom: '18%',
                        right: '5%'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    xAxis: {
                        name: 'Time/s',
                        nameLocation: 'middle',
                        nameTextStyle: {
                            fontWeight: 'bold',
                            fontSize: 14,
                            lineHeight: 10,
                            padding: [12, 5, 5, 5]
                        }
                    },
                    yAxis: {
                        name: '',
                        nameLocation: 'end',
                        nameTextStyle: {
                            fontWeight: 'bold',
                            fontSize: 14,
                            lineHeight: 10,
                            padding: [5, 5, 5, 12]
                        }
                    },
                    series: [
                        {
                            type: "line",
                            data: [],
                            symbolSize: 5
                        },
                        {
                            type: "line",
                            data: [],
                            symbolSize: 5
                        },
                    ]
                }
            }
        },

        mounted() {
            this.drawLine(this.reData1, this.reData2)
        },

        methods: {
            drawLine(data1, data2) {
                var myChart = echarts.init(this.$refs.main);
                var chart_option = this.option;
                chart_option.series[0].data = data1;
                chart_option.series[1].data = data2;
                myChart.setOption(chart_option);
            },

        },

        watch: {
            reData1: {
                handler(newdata, olddata) {
                    this.drawLine(this.reData1, this.reData2)
                },
                deep: true,
                immediate: false
            }
        },
    }
</script>