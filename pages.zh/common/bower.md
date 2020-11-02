# bower

> 前端web开发的包管理优化工具。
> 一个包可以是GitHub中user/repo的缩写，一个Git端口，一个URL链接或者一个已注册的包。
> 更多信息: <https://bower.io/>.

- 安装列在项目下 的bower.json文件中的依赖:

`bower install`

- 安装一个或者多个依赖到bower_components目录:

`bower install {{包名1}} {{包名2}}`

- 从本地的bower_components目录卸载依赖

`bower uninstall {{包名1}} {{包名2}}`

- 列出本地包和可能的更新项:

`bower list`

- 显示bower指令的帮助信息:

`bower help {{指令}}`

- 创建你的项目的bower.json:

`bower init`

- 安装时候指定依赖的版本号，并添加到bower.json:

`bower install {{local_name}}={{package}}#{{version}} --save`
