<template>
    <p>{{loadData}}</p>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Geom',
        props: { 'loadIndex': Object },
        data() {
            return {
                loadData: {},
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/load';
                axios.get(path)
                    .then((res) => {
                        this.loadData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/load';
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
            loadIndex: {
                handler(newindex, oldindex) {
                    this.postIndex(newindex);
                },
                deep: true,
            }
        }
    };
</script>