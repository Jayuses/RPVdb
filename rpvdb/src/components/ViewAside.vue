<template>
    <el-table :data="tableData.caselist"
                style="width: 95%;line-height:10px;margin-left:10px"
                height="450"
              @cell-dblclick="detail">
        <el-table-column prop="CaseID"
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
                //poststyle: { style: this.dataStyle },
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

            detail(row) {
                let index = {
                    style: this.dataStyle,
                    index: row.CaseID
                };
                this.$emit('show-detail', index);

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
