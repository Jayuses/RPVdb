<template>
    <div>
        <el-table :data="tableData.caselist"
                  :row-class-name="tableRowClassName"
                  :row-style="selectedstyle"
                  :show-header="false"
                  style="width: 95%;line-height:10%;margin-left:5%"
                  height="40em"
                  @cell-click="detail">
            <el-table-column prop="ID"
                             align="center"
                             width="200%">
            </el-table-column>
        </el-table>
    </div>
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
            selectedstyle({ _, rowIndex }) {
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
                var theindex = {};
                if (this.dataStyle == 4) {
                    theindex = {
                        style: row.style,
                        index: row.ID,
                        case: row.CaseID
                    };
                } else if (this.dataStyle == 5) {
                    theindex = {
                        style: this.dataStyle,
                        index: row.ID,
                    };
                }
                this.$emit('show-detail', theindex);
                this.getIndex = row.index
            }

        },

        watch: {
            dataStyle: {
                handler(newstyle,_) {
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
