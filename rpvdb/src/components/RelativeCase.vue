<template>
    <div>
        <el-table :data="CaseList"
                  style="width: 100%"
                  height="40em"
                  align="center">
            <el-table-column prop="case"
                             label="相关案例"
                             width="220"
                             align="center">
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