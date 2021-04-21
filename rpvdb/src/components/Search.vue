<template>
    <div>
        {{caseForm}}
        <el-form :inline="true" :model="formInline" class="demo-form-inline">
            <el-form-item label="顶盖类型">
                <el-select v-model="caseForm.style" placeholder="顶盖类型">
                    <el-option v-for="item in dingGai"
                               :key="item.value"
                               :label="item.label"
                               :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="顶盖材料">
                <el-cascader v-model="caseForm.MHead"
                             :options="mater"></el-cascader>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
    export default {
        name:'Search',
        data() {
            return {
                caseForm: {
                    style: [],
                    SG_ID: '',
                    MHead: [],
                    MRPV: [],
                    MBolt: [],
                    MLayer: [],
                    LC_ID:''
                },
                dingGai: [
                    {
                        value: 1,
                        label:'球型顶盖'
                    },
                    {
                        value: 2,
                        label: '内带平台球型顶盖'
                    },
                    {
                        value: 3,
                        label: '平顶盖'
                    },
                ],
                mater: [
                    {
                        value: '16MND5',
                        label: '16MND5',
                        children: [
                            {
                                value: '弹性',
                                label: '弹性',
                            },
                            {
                                value: '弹塑性',
                                label: '弹塑性',
                            }
                        ]
                    },
                    {
                        value: '308L309L',
                        label: '308L309L',
                        children: [
                            {
                                value: '弹性',
                                label: '弹性',
                            },
                            {
                                value: '弹塑性',
                                label: '弹塑性',
                            }
                        ]
                    },

                ]
            }
        }
    }
</script>