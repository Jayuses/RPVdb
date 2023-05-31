<template>
    <div>
        <el-row>
            <el-col :span="20">
                <div>
                    <el-table   :data="userData" 
                                style="width: 75%;margin-left:15%"
                                height="39em"
                                align="center"
                                max-height="100%" >
                        <el-table-column type="index">
                        </el-table-column>
                        <el-table-column prop="name" label="用户名" width="100%">
                            <template slot-scope="scope">
                                <el-input v-model="scope.row.name"></el-input>
                            </template>
                        </el-table-column>
                        <el-table-column prop="password" label="密码" width="250%">
                            <template slot-scope="scope">
                                <el-input v-model="scope.row.password"></el-input>
                            </template>
                        </el-table-column>
                        <el-table-column prop="level" label="等级" width="250%">
                            <template slot-scope="scope">
                                <el-select v-model="scope.row.level">
                                    <el-option   v-for="item in options"
                                                :key="item.value"
                                                :label="item.level"
                                                :value="item.level">
                                    </el-option>
                                </el-select>
                            </template>
                        </el-table-column>
                        <el-table-column label="操作" width="100%">
                            <template slot-scope="scope">
                                <div style="display: flex;justify-content: space-between;">
                                    <el-link icon="el-icon-plus" size="mini" type="primary"
                                        @click="handleAdd(scope.$index, scope.row)" :underline="false"></el-link>
                                    <el-link icon="el-icon-delete" size="mini" @click="handleDelete(scope.$index, scope.row)"
                                        type="danger" :underline="false"></el-link>
                                </div>
                            </template>
                        </el-table-column>
                    </el-table>
                    <div>
                        <span>
                            <el-button  type="primary" 
                                        style="margin-top:1em;margin-right:5%;margin-left:2%" 
                                        @click='submit'>提交修改</el-button>
                            <el-button @click="$emit('close',0)">关闭</el-button>
                        </span>
                    </div>
                </div>
            </el-col>
            <el-col :span="4">
                <div style="position:absolute;line-height:1em;top:40%;">
                    <p style="color:#E6A23C;">用户名是用户的唯一标识</p>
                    <p style="color:#E6A23C;">修改用户名相当于新建用户</p>
                    <p style="color:#E6A23C;">请同时修改密码</p>
                </div>
            </el-col>
        </el-row>  
    </div>
</template>

<style>
    
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'Users',
        props: {'dataStyle':Number},
        data() {
            return {
                options: [{value:'1',level:'administrator'},{value:'2',level:'user'}],
                userData:[],
                tempData:[],
                delcord:[],
            }
        },

        methods: {
            async getList(url) {
                //获取数据列表
                const path = 'http://localhost:5000/' + url;
                let options = [];
                await axios.get(path)
                    .then((res) => {
                        options = res.data;
                    })
                /*.catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });*/
                return options;
            },
            getData() {
                const path = 'http://localhost:5000/getdata/users';
                axios.get(path)
                    .then((res) => {
                        this.userData = this.processData(res.data);
                        this.tempData = this.processData(res.data);
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.error(error);
                    });
            },
            postReq(payload) {
                //发送数据请求
                const path = 'http://localhost:5000/getdata/users';
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
            handleAdd(index, row) {
                this.userData.push({
                        name:'',
                        password:'',
                        level:''
                    });
            },
            handleDelete(index, row) {
                if (index > 0) {
                    this.delcord.push(this.userData[index]);
                    this.userData.splice(index, 1);
                }
            },
            processData(data){
                var userData = [];
                for(var i=0;i<data.length;i++){
                    userData.push({
                        name:data[i].name,
                        password:'******',
                        level:data[i].level
                    })
                }
                return userData;
            },
            submit(){
                var modi = {delData:[],mod:[]};
                var userData = this.userData;
                var tempData = this.tempData;
                for(var i=0;i<userData.length;i++){
                    for(var j=0;j<tempData.length;j++){
                        if(tempData[j].name==userData[i].name){
                            if (tempData[j].password!=userData[i].password||tempData[j].level!=userData[i].level){
                                modi.mod.push(userData[i]);
                                break;
                            }else break;
                        }else if(j==tempData.length-1){
                            modi.mod.push(userData[i]);
                        }
                    }
                }
                modi.delData = this.delcord;
                const path = 'http://localhost:5000/login/change';
                axios.post(path, modi)
                    .then(() => {
                        this.getList('login/change').then(res => {
                            if (res == 1){
                                this.$message({
                                    message: '修改成功',
                                    type: 'success'
                                });
                            }
                            let poststyle = { style: this.dataStyle };
                            this.postReq(poststyle);
                        })
                    })


            }
        },

        computed: {
            
        },

        watch: {
            dataStyle: {
                handler(newstyle, oldstyle) {
                    let poststyle = { style: newstyle };
                    this.postReq(poststyle);
                },
                immediate:true    
            }
        },
    };
</script>