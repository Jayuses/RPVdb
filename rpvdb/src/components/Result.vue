<template>
    <p>{{resultData}}</p>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Result',
        //父组件ViewCase传入参数resultIndex{'style':'','index':''}，
        //分别表示顶盖类型与算例名称
        props: {'resultIndex':Object},
        data() {
            return {
                resultData: {},
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/result';
                axios.get(path)
                    .then((res) => {
                        this.resultData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/result';
                axios.post(path, payload)
                    .then(() => {
                        this.getData();
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                        this.getData();
                    });
            },
        },

        watch: {
            resultIndex: {
                handler(newindex, oldindex) {
                    this.postIndex(this.resultIndex);
                },
                deep: true,
            }
        },
    };
</script>