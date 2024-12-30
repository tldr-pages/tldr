# bower

> 一个针对前端网页开发优化的包管理器。
> 包可以是 GitHub 用户/仓库缩写、Git 端点、URL 或注册的包。
> 更多信息：<https://bower.io/>。

- 安装项目的依赖项，这些依赖项在其 bower.json 中列出：

`bower install`

- 将一个或多个包安装到 bower_components 目录：

`bower install {{package}} {{package}}`

- 从 bower_components 目录本地卸载包：

`bower uninstall {{package}} {{package}}`

- 列出本地包和可能的更新：

`bower list`

- 为你的包创建一个 `bower.json` 文件：

`bower init`

- 安装特定版本的依赖项，并将其添加到 `bower.json` 中：

`bower install {{local_name}}={{package}}#{{version}} --save`

- 显示特定命令的帮助信息：

`bower help {{command}}`