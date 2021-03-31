<template>
    <el-table :data="showList"
                style="width: 95%;line-height:10px;margin-left:10px"
                height="450">
        <el-table-column prop="CaseID"
                            align="center"
                            width="215">
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

        },

        computed: {
            showList() {
                //动态展示数据列表
                let poststyle={ style: this.dataStyle }
                this.postReq(poststyle);
                //var datalist = this.tableData['datalist'];
                return   this.tableData.caselist
            },

            showName() {
                //动态展示表名
                switch (this.dataStyle) {
                    case 1: return ('球形顶盖');
                }
            },

            showClomn() {
                //列名切换
                switch (this.dataStyle) {
                    case 1:
                    case 2:
                    case 3:
                        return ("CaseID");
                    case 4:
                        return("SG_ID")
                }
            }
        },

        /*created() {
            this.postReq(this.poststyle);
        }*/
    };
</script>
