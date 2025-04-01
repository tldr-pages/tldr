# pee

> 将 `stdin` 同时输出到多个管道。
> 参见：`tee`。
> 更多信息：<https://joeyh.name/code/moreutils/>。

- 运行每个命令，每个命令使用 `stdin` 的一个独立副本：

`pee {{command1 command2 ...}}`

- 将 `stdin` 的副本写入 `stdout`（类似 `tee`）：

`pee cat {{command1 command2 ...}}`

- 在接收到 SIGPIPE 信号或写入错误时立即终止：

`pee --no-ignore-sigpipe --no-ignore-write-errors {{command1 command2 ...}}`