# runlim

> 使用 Linux 的 proc 文件系统对程序及其子进程的时间和内存使用进行采样和限制。
> 更多信息：<https://fmv.jku.at/runlim>。

- 打印命令的时间和内存使用：

`runlim {{command}} {{command_arguments}}`

- 将统计信息记录到文件中，而不是 `stdout`：

`runlim --output-file={{path/to/file}} {{command}} {{command_arguments}}`

- 将时间限制为上限（以秒为单位）：

`runlim --time-limit={{number}} {{command}} {{command_arguments}}`

- 将实际时间限制为上限（以秒为单位）：

`runlim --real-time-limit={{number}} {{command}} {{command_arguments}}`

- 将空间限制为上限（以 MB 为单位）：

`runlim --space-limit={{number}} {{command}} {{command_arguments}}`