<template>
    <div>
        <div ref="main" style="width: 600px;height:350px;margin-top:5em;margin-left:12em"></div>
    </div>
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
        name: 'MaterChart',
        props: [ 'chartData','materUnit'] ,
        data() {
            return {
                option: {
                    grid: {
                        top: '10%',
                        left:'15%'
                    },
                    tooltip: {
                        trigger:'axis'
                    },
                    xAxis: {
                        name: 'Temperature/℃',
                        nameLocation: 'middle',
                        nameTextStyle: {
                            fontWeight: 'bold',
                            fontSize: 14,
                            lineHeight: 10,
                            padding:[15,5,5,5]
                        }
                    },
                    yAxis: {
                        name:'',
                        nameLocation: 'middle',
                        nameTextStyle: {
                            fontWeight: 'bold',
                            fontSize: 14,
                            lineHeight: 10,
                            padding: [5, 5, 25, 5]
                        }
                    },
                    series: [
                        {
                            type: "line",
                            data: [],
                            symbolSize:5
                        },
                    ]
                }
            }
        },

        mounted() {
            this.drawLine(this.chartData,this.materUnit)
        },

        methods: {
            drawLine(data,unit) {
                var myChart = echarts.init(this.$refs.main);
                var chart_option = this.option;
                chart_option.series[0].data = data;
                chart_option.yAxis.name = unit;
                myChart.setOption(chart_option);   
            },

        },

        watch: {
            chartData: {
                handler(newdata,_) {
                    this.drawLine(newdata, this.materUnit)
                },
                deep: true,
                immediate: false,
            }
        },
    }
</script>