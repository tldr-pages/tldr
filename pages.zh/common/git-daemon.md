# git 守护进程

> 一个非常简单的 Git 仓库服务器。
> 更多信息：<https://git-scm.com/docs/git-daemon>。

- 启动一个 Git 守护进程，并指定一个白名单目录集：

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- 启动一个 Git 守护进程，指定一个基本目录，并允许从所有看起来像 Git 仓库的子目录中拉取：

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- 为指定目录启动一个 Git 守护进程，详细打印日志消息，并允许 Git 客户端写入：

`git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose`