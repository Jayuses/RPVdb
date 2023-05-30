<template>
    <div>
        <el-collapse  accordion>
            <el-collapse-item name="1">
                <template slot="title">
                    <p class="accordion">
                        瞬态工况
                    </p>
                </template>
                <el-table :data="tableData1.LC"
                          :row-class-name="tableRowClassName"
                          :row-style="selectedstyle"
                          :show-header="false"
                          style="width: 95%;line-height:10%;margin-left:5%"
                          @cell-click="detail">
                    <el-table-column prop="ID"
                                     align="center"
                                     width="200%">
                    </el-table-column>
                </el-table>
            </el-collapse-item>
            <el-collapse-item name="2">
                <template slot="title">
                    <p class="accordion">
                        设计工况
                    </p>
                </template>
                <el-table :data="tableData2.LC"
                          :row-class-name="tableRowClassName"
                          :row-style="selectedstyle"
                          :show-header="false"
                          style="width: 95%;line-height:10%;margin-left:5%"
                          @cell-click="detail">
                    <el-table-column prop="ID"
                                     align="center"
                                     width="200%">
                    </el-table-column>
                </el-table>
            </el-collapse-item>
            <el-collapse-item name="3">
                <template slot="title">
                    <p class="accordion">
                        水压试验工况
                    </p>
                </template>
                <el-table :data="tableData3.LC"
                          :row-class-name="tableRowClassName"
                          :row-style="selectedstyle"
                          :show-header="false"
                          style="width: 95%;line-height:10%;margin-left:5%"
                          @cell-click="detail">
                    <el-table-column prop="ID"
                                     align="center"
                                     width="200%">
                    </el-table-column>
                </el-table>
            </el-collapse-item>
            
        </el-collapse>
    </div>
</template>

<style>
    .accordion{
        line-height:16px;
        font-weight:700;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'LoadLibrary',
        props: { 'dataStyle': Number },
        data() {
            return {
                tableData1: {},
                tableData2: {},
                tableData3: {},
                getIndex: '',
                test:0,

            }
        },

        methods: {
            getList() {
                //获取数据列表
                const path = 'http://localhost:5000/getdata/list';
                axios.get(path)
                    .then((res) => {
                        this.test = 2;
                        this.tableData1 = res.data.caselist[0];
                        this.tableData2 = res.data.caselist[1];
                        this.tableData3 = res.data.caselist[2];
                    })
                /*.catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });*/
            },

            postReq(payload) {
                //发送数据请求，数据类型由dataStyle控制
                const path = 'http://localhost:5000/getdata/list';
                axios.post(path, payload)
                    .then(() => {
                        this.test = 1;
                        this.getList()
                    })
                /*.catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                    this.getList()
                });*/
            },
            selectedstyle({ row, rowIndex }) {
                if ((this.getIndex) === rowIndex) {
                    return {
                        "background-color": "#E0E0E0"
                    };
                }
            },

            tableRowClassName({ row, rowIndex }) {
                row.index = rowIndex;
            },

            rowClick(row) {
                this.getIndex = row.index
            },

            detail(row) {
                let theindex = {
                    style: row.style,
                    index: row.ID,
                    case:row.CaseID
                };
                this.$emit('show-detail', theindex);
                this.getIndex = row.index
            }

        },

        watch: {
            dataStyle: {
                handler(newstyle, oldstyle) {
                    let poststyle = { style: newstyle };
                    this.postReq(poststyle);
                },
                immediate: true,
            }
        },

        /*created() {
            let poststyle = { style: this.dataStyle };
            this.postReq(poststyle);
        }*/
    };
</script>
