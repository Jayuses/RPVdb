<template>
    <div class="login-container">
        <h4>用户登录</h4>
        <el-form :model="logForm" status-icon  :rules="rules" ref="logForm" label-width="100px" class="demo-ruleForm">
            <el-form-item label="用户名" prop="username">
                <el-input type="text" v-model="logForm.username" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input type="password" v-model="logForm.password" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item class="button-item">
                <el-button type="primary" @click="submitForm('logForm')">登录</el-button>
                <el-button @click="resetForm('logForm')">取消</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<style>
    .login-container {
        box-shadow: 0 8px 16px rgba(0, 0, 0, .12), 0 0 24px rgba(0, 0, 0, .04);
        position:absolute;
        top: 25%;
        bottom: 30%;
        left: 35%;
        right: 35%;
    }
    h4{
        margin-top:10%;
    }
    .el-form-item__label{
        max-width:70px;
        margin-left:15px;
    }
    form {
        margin-right: 10%;
    }
    .button-item{
        margin-left:-60px;
    }
</style>

<script>
    import axios from 'axios';
    export default {
        name: 'Login',
        data() {
            //定义验证器 checkname,checkpass
            var checkname = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入用户名'));
                } else {
                    callback();
                }
            };
            var checkpass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    const path = 'http://localhost:5000/login/';
                    axios.post(path, this.logForm)
                        .then(() => {
                            axios.get(path)
                                .then((res) => {
                                    if (res.data.status === 0) {
                                        callback(new Error('密码错误'));
                                    } else if (res.data.status === 2) {
                                        callback(new Error('用户名不存在'));
                                    } else if (res.data.status === 1) {
                                        this.logClass = res.data.class
                                        callback();
                                    }
                                })
                                .catch((error) => {
                                    // eslint-disable-next-line
                                    console.error(error);
                                });
                        })
                        .catch((error) => {
                            // eslint-disable-next-line
                            console.error(error);
                        });
                }
            };
            return {
                logForm: {
                    username: '',
                    password:''
                },
                rules: {
                    username: [
                        { validator: checkname, trigger: 'blur' },
                    ],
                    password: [
                        { validator: checkpass, trigger: 'blur' },
                    ]
                },
                logClass : -1
            }
        },
        methods: {
            submitForm(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        this.$router.push({ name: 'Home', params: { logClass: this.logClass } });
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }

        }
    };
</script>