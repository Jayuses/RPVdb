<template>
    <div class="home">
        <el-container>
            <el-header>
                <el-tabs type="border-card" value="first" >
                    <el-tab-pane label="查看" name="first">
                        <el-row :gutter="20">
                            <el-col :span="7" style="border-right: 1px solid #C0C0C0">
                                <h5>查看算例</h5>
                                <span>
                                    <el-button type="text" @click="datastyle=1"> 球形顶盖 </el-button>
                                    <el-button type="text" @click="datastyle=2"> 内带平台球形顶盖 </el-button>
                                    <el-button type="text" @click="datastyle=3"> 平顶盖 </el-button>
                                </span>
                            </el-col>
                            <el-col :span="7" style="border-right: 1px solid #C0C0C0">
                                <h5>结构尺寸</h5>
                                <span>
                                    <el-button type="text" @click="datastyle=4"> SG-系列 </el-button>
                                    <el-button type="text" @click="datastyle=5"> SG-D-系列 </el-button>
                                    <el-button type="text" @click="datastyle=6"> 其他 </el-button>
                                </span>
                            </el-col>
                            <el-col :span="5" style="border-right: 1px solid #C0C0C0">
                                <h5>结构材料</h5>
                                <span>
                                    <el-button type="text" @click="datastyle=7"> 材料库 </el-button>
                                </span>
                            </el-col>
                            <el-col :span="5">
                                <h5>加载工况</h5>
                                <span>
                                    <el-button type="text" @click="datastyle=8"> 加载工况库 </el-button>
                                </span>
                            </el-col>
                        </el-row>
                    </el-tab-pane>
                    <el-tab-pane label="输入" name="second">输入数据</el-tab-pane>
                </el-tabs>
            </el-header>
            <br /><br /><br /><br />
            <el-container>
                <el-aside width="250px" style="border-right: 2px solid #C0C0C0">
                    <ViewAside :dataStyle="datastyle"></ViewAside>
                </el-aside>
                <el-main></el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style>
    .el-header {
        text-align: center;
        line-height: 100%;
    }
    .el-aside {
        margin-left:21px;
        text-align: center;
        line-height: 160px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    .el-main {
        margin-right: 21px;
        text-align: center;
        line-height: 160px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    h5{
        margin-top:4px;
        margin-bottom:4px;
    }
</style>

<script>
import ViewAside from '../components/ViewAside.vue'
export default {
    name: 'Home',
    data() {
        return {
            datastyle:0
        };
    },

    components: {
        ViewAside
    }
}
</script>
