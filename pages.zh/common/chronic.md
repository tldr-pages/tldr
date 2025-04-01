# chronic

> 仅在命令失败时显示 `stdout` 和 `stderr`。
> 更多信息：<https://manned.org/chronic>.

- 仅在指定命令产生非零退出码或崩溃时显示 `stdout` 和 `stderr`：

`chronic {{command options ...}}`

- 仅在指定命令产生非空 `stderr` 时显示 `stdout` 和 `stderr`：

`chronic -e {{command options ...}}`

- 启用 [v]erbose 模式：

`chronic -v {{command options ...}}`