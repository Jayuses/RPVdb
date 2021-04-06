<template>
    <el-row :gutter="10" class="materRow">
        <el-col :span="5">
            <div class="materClomn1">
                <!--<h4>项目</h4>-->
                <p>顶盖材料<br />筒体材料<br />紧固件材料<br />堆焊层材料</p>
            </div>
        </el-col>
        <el-col :span="4">
            <div class="materClomn">
                <!--<h4>选用材料</h4>-->
                <p style="height:200px">
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
                               width="30%">
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
        height:350px;
    }
    h4{
        margin:10px;
    }
</style>

<script>
    import axios from 'axios';
    import MaterDetail from './MaterDetail.vue'
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

        components: {
            MaterDetail,
        }
    };
</script>