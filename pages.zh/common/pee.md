# pee

> 将 `stdin` 分配给管道。
> 另请参见：`tee`。
> 更多信息：<https://joeyh.name/code/moreutils/>.

- 运行每个命令，为每个命令提供 `stdin` 的独立副本：

`pee {{command1 command2 ...}}`

- 将 `stdin` 的副本写入 `stdout`（类似于 `tee`）：

`pee cat {{command1 command2 ...}}`

- 在接收到 SIGPIPE 信号时立即终止并写入错误：

`pee --no-ignore-sigpipe --no-ignore-write-errors {{command1 command2 ...}}`