<template>
    <el-table :data="tableData.caselist"
              :row-class-name="tableRowClassName" 
              :row-style="selectedstyle"
              :show-header="false"
              style="width: 95%;line-height:10px;margin-left:10px"
              height="430px"
              @cell-dblclick="detail">
        <el-table-column prop="ID"
                          align="center"
                          width="170">
        </el-table-column>
    </el-table>
</template>

<style>
    .el-tabs--border-card > .el-tabs__content {
        padding: 10px;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'ViewAside',
        props: { 'dataStyle': Number },
        data() {
            return {
                tableData: {},
                getIndex: ''
            }
        },

        methods: {
            getList() {
                //获取数据列表
                const path = 'http://localhost:5000/getdata/list';
                axios.get(path)
                    .then((res) => {
                        this.tableData = res.data;
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
                    style: this.dataStyle,
                    index: row.ID
                };
                this.$emit('show-detail', theindex);
                this.getIndex = row.index
            }

        },

        watch: {
            dataStyle(newstyle, oldstyle) {
                let poststyle = { style: newstyle };
                this.postReq(poststyle);
            }
        },

        /*created() {
            let poststyle = { style: this.dataStyle };
            this.postReq(poststyle);
        }*/
    };
</script>
