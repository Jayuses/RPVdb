<template>
    <div id="app">
        <keep-alive>
            <router-view v-if="$route.meta.keepAlive && isRouterAlive" :key="key"></router-view>
        </keep-alive>
            <router-view v-if="!$route.meta.keepAlive && isRouterAlive" :key="key"></router-view>
    </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<script>
    export default {
        name: 'App',
        provide() {                                                
            return {
                reload: this.reload
            }
        },
        data() {
            return {
                isRouterAlive: true    
            }
        },
        methods: {
            reload() {
                this.isRouterAlive = false;       
                this.$nextTick(function () {
                    this.isRouterAlive = true;     
                })
            }
        },
        computed:{
            key() {
                return this.$route.name !== undefined ? 
                this.$route.name + +new Date(): this.$route + +new Date()
            }
        }
    }
</script>
