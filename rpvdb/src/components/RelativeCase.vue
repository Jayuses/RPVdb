<template>
    <div>
        <el-table :data="CaseList"
                  style="width: 100%"
                  height="430px">
            <el-table-column prop="case"
                             label="相关案例"
                             width="150">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
    export default {
        name: 'RelativeCase',
        props: { 'CaseList': Array },
        data() {
            return {
                
            }
        },
    }
</script>