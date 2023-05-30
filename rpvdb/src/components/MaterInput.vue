<template>
    <div>
        <el-table :data="selfData" 
                  style="width: 100%;"
                  height="40em"
                  align="center"
                  max-height="100%" >
            <el-table-column prop="T" label="温度">
                <template slot-scope="scope">
                    <el-input v-model="scope.row.T"></el-input>
                </template>
            </el-table-column>
            <el-table-column prop="value" label="值">
                <template slot-scope="scope">
                    <el-input v-model="scope.row.value"></el-input>
                </template>
            </el-table-column>
            <el-table-column label="操作" width="70%">
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
    </div>
</template>

<script>
    export default {
        name: 'MaterInput',
        props: { 'propIndex': String ,'materData':Array},
        data() {
            return {
                selfData: this.materData
            }
        },
        methods:{
            handleAdd(index, row) {
                this.selfData.push({
                    T: '',
                    value:''
                });
            },
            handleDelete(index, row) {
                if (index > 0) {
                    this.selfData.splice(index, 1);
                }
            },
        },
        watch: {
            propIndex: {
                handler(newindex, oldindex) {
                    this.$emit('materTemp',this.selfData);

                },
                immediate:true
            },
            materData:{
                handler(newindex, oldindex) {
                    this.selfData = newindex;
                },
                immediate:true
            }
        }
    }
</script>