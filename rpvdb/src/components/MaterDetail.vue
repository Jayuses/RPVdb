<template>
    <p>{{materData}}</p>
</template>

<script>
    import axios from 'axios';
    export default {
        name: 'MaterDetail',
        props: {'materIndex':String},
        data() {
            return {
                materData: {},
            }
        },

        methods: {
            getData() {
                //获取结构参数
                const path = 'http://localhost:5000/getdata/mater';
                axios.get(path)
                    .then((res) => {
                        this.materData = res.data;
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },

            postIndex(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/mater';
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
            materIndex: {
                handler(newindex, oldindex) {
                    let index = { index: newindex };
                    this.postIndex(index);
                },
                immediate:true
            }
        },
    };
</script>