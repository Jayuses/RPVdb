<template>
    <div>
        <p>{{chartData}}</p>
        <div id="main" style="width: 400px;height:400px;"></div>
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
        [TitleComponent, TooltipComponent, GridComponent,LineChart, ScatterChart, CanvasRenderer]
    );
     //vue文件中引入echarts工具
    export default {
        name: 'MaterChart',
        props: ['chartData'] ,
        data() {
            return { 
                option: {
                    xAxis: {
                        type: 'value',
                    },
                    yAxis: {
                        type: 'value'
                    },
                    dataset: {
                        source: [[20, 78], [100, 78], [200, 78], [300, 78], [350, 78]] 
                    },          
                    series: [
                        {
                            type: 'scatter',
                            symbol: 'circle',
                            encode: { x: 0, y: 1 }
                        },
                        {
                            type: 'line',
                            encode: { x: 0, y: 1 }
                        }
                    ]
                }
            }
        },

        mounted() {
            this.drawLine()
        },

        methods: {
            drawLine() {
                var myChart = echarts.init(document.getElementById('main'));
                myChart.setOption(this.option);   
            }
        }
    }
</script>