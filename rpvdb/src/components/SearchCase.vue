<template>
    <el-table :data="caselist"
              :row-class-name="tableRowClassName"
              :row-style="selectedstyle"
              :show-header="false"
              style="width: 95%;line-height:10px;margin-left:10px"
              height="430px"
              @cell-dblclick="detail">
        <el-table-column prop="CaseID"
                         align="center"
                         width="170">
        </el-table-column>
    </el-table>
</template>

<style>
    .el-tabs--border-card > .el-tabs__content {
        padding: 10px;
    }
</style>

<script>
    export default {
        name: 'SearchCase',
        props: { 'caselist': Object },
        data() {
            return {
                getIndex: ''
            }
        },
        methods: {
            selectedstyle({ row, rowIndex }) {
                if ((this.getIndex) === rowIndex) {
                    return {
                        "background-color": "#E0E0E0"
                    };
                }
            },

            tableRowClassName({ row, rowIndex }) {
                row.index = rowIndex;
            },

            rowClick(row) {
                this.getIndex = row.index
            },

            detail(row) {
                let theindex = {
                    style: row.style,
                    index: row.CaseID
                };
                this.$emit('show-detail', theindex);
                this.getIndex = row.index
            }

        },
    }
</script>