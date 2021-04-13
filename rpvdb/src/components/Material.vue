<template>
    <div>
        <el-row class="materRow">
            <el-col :span="5" :offset="5">
                <div class="materClomn1">
                    <!--<h4>项目</h4>-->
                    <p>顶盖材料<br />筒体材料<br />紧固件材料<br />堆焊层材料</p>
                </div>
            </el-col>
            <el-col :span="4">
                <div class="materClomn">
                    <!--<h4>选用材料</h4>-->
                    <p>
                        <el-button type="text" @click="dialog(materInfor.MHead)">
                            {{materInfor.MHead}}
                        </el-button><br />
                        <el-button type="text" @click="dialog(materInfor.MRPV)">
                            {{materInfor.MRPV}}
                        </el-button><br />
                        <el-button type="text" @click="dialog(materInfor.MBolt)">
                            {{materInfor.MBolt}}
                        </el-button><br />
                        <el-button type="text" @click="dialog(materInfor.MLayer)">
                            {{materInfor.MLayer}}
                        </el-button>
                        <el-dialog :visible.sync="dialogVisible"
                                   width="60%">
                            <MaterDetail :materIndex="materIndex"></MaterDetail>
                        </el-dialog>
                    </p>
                </div>
            </el-col>
            <el-col :span="4">
                <div class="materClomn">
                    <!--<h4>分析模式</h4>-->
                    <p>
                        {{materInfor.MHeadAM}}分析<br />
                        {{materInfor.MRPVAM}}分析<br />
                        {{materInfor.MBoltAM}}分析<br />
                        {{materInfor.MLayerAM}}分析
                    </p>
                </div>
            </el-col>
        </el-row>
        <el-image style="width: 472px; height: 180px"
              :src="url"></el-image>
    </div>
</template>

<style>
    .materClomn1{
        padding:4px;
        line-height:40px;
        font-weight:500;
        height:100%;
    }
    .materClomn {
        padding: 4px;
        line-height: 40px;
    }
    .materRow{
        height:180px;
    }
        .materRow p {
            margin-top: 0px;
            margin-bottom: 5px;
        }
    h4{
        margin:10px;
    }
</style>

<script>
    import axios from 'axios';
    import MaterDetail from './MaterDetail.vue';
    export default {
        name: 'Material',
        props: { 'materInfor': Object },
        data() {
            return {
                materData: {},
                materIndex: '',
                dialogVisible:false,
            }
        },

        methods: {
            dialog(mater) {
                this.dialogVisible = true;
                this.materIndex = mater;
            }
        },

        computed: {
            url() {
                if (this.materInfor.style == 1)
                    return require('../assets/image/path1/球形顶盖_材料选择示意图.png');
                else if (this.materInfor.style == 2)
                    return require('../assets/image/path2/内带平台球形顶盖_材料选择示意图.png');
                else if (this.materInfor.style == 3)
                    return require('../assets/image/path3/平顶盖-材料选择示意图.png');
            }
        },

        components: {
            MaterDetail
        }
    };
</script>