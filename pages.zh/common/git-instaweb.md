# git instaweb

> 启动 GitWeb 服务器的助手。
> 更多信息：<https://git-scm.com/docs/git-instaweb>。

- 为当前 Git 仓库启动 GitWeb 服务器：

`git instaweb --start`

- 仅在本地主机上监听：

`git instaweb --start --local`

- 在特定端口上监听：

`git instaweb --start --port {{1234}}`

- 使用指定的 HTTP 守护进程：

`git instaweb --start --httpd {{lighttpd|apache2|mongoose|plackup|webrick}}`

- 还自动启动网页浏览器：

`git instaweb --start --browser`

- 停止当前运行的 GitWeb 服务器：

`git instaweb --stop`

- 重启当前运行的 GitWeb 服务器：

`git instaweb --restart`