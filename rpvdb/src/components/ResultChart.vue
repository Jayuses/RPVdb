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
        DataZoomComponent,
        GraphicComponent
    } from 'echarts/components';
    // 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
    import {
        CanvasRenderer
    } from 'echarts/renderers';
    //注册必须的组件
    echarts.use(
        [TitleComponent, TooltipComponent, GridComponent, DataZoomComponent, GraphicComponent, LineChart, ScatterChart, CanvasRenderer]
    );
    export default {
        name: 'ResultChart',
        props: {
            'reData': Array,
            'process': String,
            'reUnit': String,
        },
        data() {
            return {
                option: {
                    grid: {
                        top:'5%',
                        left: '15%',
                        bottom: '18%',
                        right:'5%'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    xAxis: {
                        name: '',
                        nameLocation: 'middle',
                        nameTextStyle: {
                            fontWeight: 'bold',
                            fontSize: 14,
                            lineHeight: 10,
                            padding: [15, 5, 5, 5]
                        }
                    },
                    yAxis: {
                        name: '',
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
                            symbolSize: 5
                        },
                    ],
                    dataZoom: [
                        {
                            type: 'slider',
                            show: false,
                            xAxisIndex: 0,
                            filterMode: 'none'
                        },
                        {
                            type: 'slider',
                            show: false,
                            yAxisIndex: 0,
                            filterMode: 'none'
                        },
                        {
                            type: 'inside',
                            show: false,
                            xAxisIndex: 0,
                            filterMode: 'none'
                        },
                        {
                            type: 'inside',
                            show: false,
                            yAxisIndex: 0,
                            filterMode: 'none'
                        }
                    ],
                }
            }
        },

        mounted() {
            this.drawLine(this.reData)
        },

        methods: {
            drawLine(data) {
                var myChart = echarts.init(this.$refs.main);
                var chart_option = this.option;
                chart_option.series[0].data = data;
                chart_option.xAxis.name = this.process;
                chart_option.yAxis.name = this.reUnit;
                myChart.setOption(chart_option);
                this.drag_larger(myChart, data);
            },

            drag_larger(myChart, data) {
                setTimeout(function (data) {
                    // Add shadow circles (which is not visible) to enable drag.
                    myChart.setOption({
                        graphic: echarts.util.map(data, function (item, dataIndex) {
                            return {
                                type: 'circle',
                                position: myChart.convertToPixel('grid', item),
                                shape: {
                                    cx: 0,
                                    cy: 0,
                                },
                                invisible: true,
                                draggable: true,
                                ondrag: function (dx, dy) {
                                    onPointDragging(dataIndex, [this.x, this.y]);
                                },
                                z: 100
                            };
                        })
                    });
                }, 0);

                window.addEventListener('resize', updatePosition);

                myChart.on('dataZoom', updatePosition);

                function updatePosition(data) {
                    myChart.setOption({
                        graphic: echarts.util.map(data, function (item, dataIndex) {
                            return {
                                position: myChart.convertToPixel('grid', item)
                            };
                        })
                    });
                }

                function onPointDragging(dataIndex, pos) {
                    data[dataIndex] = myChart.convertFromPixel('grid', pos);

                    // Update data
                    myChart.setOption({
                        series: [{
                            id: 'a',
                            data: data
                        }]
                    });
                }
            }
        },

        watch: {
            reData: {
                handler(newdata, olddata) {
                    this.drawLine(newdata)
                },
                deep: true,
                immediate: false
            }
        },
    }
</script>