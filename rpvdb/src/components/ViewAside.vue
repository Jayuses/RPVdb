<template>
    <el-table :data="showlist"
              style="width: 100%;line-height:5px"
              height="450">
        <el-table-column fixed
                         prop="CaseID"
                         lable=""
                         width="200">
        </el-table-column>
    </el-table>
</template>

<style>

</style>

<script>
    import axios from 'axios';
    export default {
        name: 'ViewAside',
        props: { 'dataStyle': Number },
        data() {
            return {
                tableData: {},
                poststyle: { style: this.dataStyle },
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
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postReq(payload) {
                //发送数据请求，数据类型由dataStyle控制
                const path = 'http://localhost:5000/getdata/list';
                if (payload.style != 0) {
                    axios.post(path, payload)
                        .then(() => {
                            this.getList()
                        })
                        .catch((error) => {
                            // eslint-disable-next-line
                            console.error(error);
                            this.getList()
                        });
                }
                else {
                    this.tableData = -1;
                }
            },

        },

        computed: {
            showlist() {
                //动态展示数据列表
                this.postReq(this.poststyle);
                //var datalist = this.tableData['datalist'];
                return   this.tableData.caselist
            },
        },

        /*created() {
            this.postReq(this.poststyle);
        }*/
    };
</script>
