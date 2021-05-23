<template>
    <div>
        <p style="color:darkgreen;line-height:30px">请从以下选项中选择一条或多条数据</p>
        <div>
            <el-table v-if="datastyle==7"
                      :data="selection"
                      :show-header="false"
                      class="tables"
                      height="300px"
                      @cell-dblclick="detail">
                <el-table-column type="selection"
                                 align="center"
                                 width="30">
                </el-table-column>
                <el-table-column prop="CaseID"
                                 align="center"
                                 width="340">
                </el-table-column>
            </el-table>
            
        </div>
    </div>
</template>

<style>
    .tables {
        width: 40%;
        line-height: 10px;
        margin-left: 10px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, .12), 0 0 24px rgba(0, 0, 0, .04);
        margin-left:6%;
    }
</style>

<script>
    export default {
        name: 'DelectCase',
        props: { 'selection': Object ,'datastyle':Number},
        data() {
            return {

            }
        }
    }
</script>