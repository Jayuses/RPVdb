# RPVdb
## 毕业设计

***

### 项目布局  
/ RPVdb  
|-----server/  
|　　　　|---flaskr/ 
|　　　　|　　　|---＿init＿.py   
|　　　　|　　　|---db.py   
|　　　　|　　　|---getdata.py   
|　　　　|　　　|---create.py   
|　　　　|　　　|---login.py   
|　　　　|　　　|---search.py  
|　　　　|  
|　　　　|---instance/       
|　　　　　　　　    
|-----rpvdb/  
|　　　　|-----src/   
|　　　　|　　　|---components/   
|　　　　|　　　|　　　　　|---ViewAside.vue   
|　　　　|　　　|　　　　　|---ViewCase.vue    
|　　　　|　　　|　　　　　|---Geom.vue  
|　　　　|　　　|　　　　　|---Material.vue  
|　　　　|　　　|　　　　　|---MaterDetail.vue  
|　　　　|　　　|　　　　　|---Load.vue  
|　　　　|　　　|　　　　　|---Result.vue  
|　　　　|　　　|　　　......   
|　　　　|　　　|　　  
|　　　　|　　　|-------router/    
|　　　　|　　　|　　　　　|---index.js    
|　　　　|　　　|-------views/   
|　　　　|　　　|　　　　　|---Home.vue   
|　　　　|　　　|　　　　　|---Dataset.vue   
|　　　　|　　　|　　　　　|---login.vue   
|　　　　|　　　|---App.vue    
|　　　　|　　　|---main.js    
|　　　　|---其他配置文件    
|  
|-----README.md  

***
### 组件树
<kbd>APP</kbd>   
　|--<kbd>Home</kbd>  
　|　　|---<kbd>ViewAside</kbd>  
　|　　|---<kbd>ViewCase</kbd>  
　|　　|　　　|---<kbd>Geom</kbd>  
　|　　|　　　|---<kbd>Material</kbd>    
　|　　|　　　|　　　|---<kbd>MaterDetail</kbd>   
　|　　|　　　|---<kbd>Load</kbd>  
　|　　|　　　|　　　|---<kbd>TP</kbd>   
　|　　|　　　|---<kbd>Result</kbd>  
　|　　|　　　|　　　|---<kbd>ResultChart</kbd>   
　|　　|　　　|　　　|---<kbd>ResultCharts</kbd>   
　|　　|---<kbd>Search</kbd>  
　|　　|---<kbd>SearchCase</kbd>  
　|　　|---<kbd>CreateCase</kbd>   
　|　　|---<kbd>DeleteCase</kbd>   
　|　　   
　|--<kbd>DataBase</kbd>  
　|　　|---<kbd>LibraryList</kbd>  
　|　　|---<kbd>LoadLibrary</kbd>  
　|　　|---<kbd>MaterDetail</kbd>  
　|　　|　　　|---<kbd>MaterDetail</kbd>   
　|　　|---<kbd>Load</kbd>  
　|　　|　　　|---<kbd>TP</kbd>   
　|　　|---<kbd>RelativeCase</kbd>  
　|　　|---<kbd>Geom</kbd>  
　|　　|---<kbd>CreateDB</kbd>  
　|　　|---<kbd>DeleteDB</kbd>  
　|　　   
　|--<kbd>Login</kbd>  
 
 
<kbd>APP</kbd>   
　|--<kbd>Login</kbd>  
　|--<kbd>Home</kbd>  
　|--<kbd>DataBase</kbd>  
 
***


### 项目进度  
+ 3.29  
    1. 前端主页面布局及部分内容的编写(Home.vue)。  
    2. ViewAside.vue部分内容的编写，包括  
       1. 发送AJAX请求相关数据列表，显示在侧边栏中  
       2. 伴随父组件(Home.vue)请求指令动态变化（仍需调试）  
    3. 后端服务器搭建(__init__.py)以及数据库连接(db.py)，现已实现将ViewAside.vue请求数据列表发送至前端(getdata.py)
    4. 现项目基于vue.js与flask环境  
        1. flask环境基于python3.8.5,新添加包有pypyodbc(用于读取.mdb数据库文件),flask_cors拓展(用于接收跨域请求)
        2. vue.js由vue.cli搭建,新添加包有element-ui,axios(发送Ajax请求)
+ 4.6  
    1. '查看'菜单修改，调整查看算例与其余库的关系。  
    2. 新增vue组件（以下组件均已完成数据连接，尚需设计界面）:  
        1. ViewCase.vue，展示算例数据的主要组件，包括多个子组件。
        2. Geom.vue，展示算例结构尺寸参数。
        3. Material.vue，展示算例结构材料参数，材料细节数据可通过子组件MaterDetial.vue显示。
        4. Load.vue，展示算例加载工况参数。
        5. Result.vue，展示算例仿真结果参数。
    3. getdata蓝图下新增多个视图,包括（用于连接数据库，接受前端请求并发送数据）：
        1. './case'算例信息
        2. './geom'结构尺寸
        3. './mater'材料数据
        4. './result'仿真结果
        5. './load'加载工况
    4. 实现数据响应更新，当用户双击某条算例时，所有数据会同时更新。  
+ 4.14   
    1. 增加登录界面，后端添加登录蓝图'login.py'，对前端用户名及密码进行验证。  
    2. 若干数据显示组件添加模板。  
    3. 新增vue组件：
        1. MaterChart.vue,用于展示材料数据图表。
        2. TP.vue，用于绘制加载工况展示中的温度压力-时间曲线。
        3. ResultChart.vue,用于绘制仿真结果曲线。

