# git daemon

> 一个非常简单的 Git 仓库服务器。
> 更多信息：<https://git-scm.com/docs/git-daemon>。

- 启动一个带有白名单目录集的 Git 守护进程：

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- 启动一个 Git 守护进程，指定基础目录并允许从所有看起来像 Git 仓库的子目录中拉取：

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- 启动一个 Git 守护进程，指定目录，详细打印日志消息并允许 Git 客户端写入：

`git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose`