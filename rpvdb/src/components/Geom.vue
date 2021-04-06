<template>
    <p>{{geomData}}</p>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'Geom',
        props: {'geomIndex':String},
        data() {
            return {
                geomData: {},
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/geom';
                axios.get(path)
                    .then((res) => {
                        this.geomData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/geom';
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
            geomIndex: {
                handler(newindex, oldindex) {
                    let index = { index: newindex };
                    this.postIndex(index);
                },
                deep: true,
            }
        },
    };
</script>