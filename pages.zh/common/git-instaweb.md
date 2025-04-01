# git instaweb

> 用于启动 GitWeb 服务器的辅助工具。
> 更多信息：<https://git-scm.com/docs/git-instaweb>。

- 为当前 Git 仓库启动 GitWeb 服务器：

`git instaweb --start`

- 仅监听本地主机：

`git instaweb --start --local`

- 监听特定端口：

`git instaweb --start --port {{1234}}`

- 使用指定的 HTTP 守护进程：

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- 同时自动启动网页浏览器：

`git instaweb --start --browser`

- 停止当前正在运行的 GitWeb 服务器：

`git instaweb --stop`

- 重启当前正在运行的 GitWeb 服务器：

`git instaweb --restart`