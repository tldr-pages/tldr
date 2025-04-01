# runlim

> 使用 Linux 的 proc 文件系统来采样并限制程序及其子进程的时间和内存使用。
> 更多信息：<https://fmv.jku.at/runlim>.

- 打印命令的时间和内存使用情况：

`runlim {{command}} {{command_arguments}}`

- 将统计信息记录到文件而不是 `stdout`：

`runlim --output-file={{path/to/file}} {{command}} {{command_arguments}}`

- 限制时间上限（以秒为单位）：

`runlim --time-limit={{number}} {{command}} {{command_arguments}}`

- 限制实时时间上限（以秒为单位）：

`runlim --real-time-limit={{number}} {{command}} {{command_arguments}}`

- 限制空间上限（以 MB 为单位）：

`runlim --space-limit={{number}} {{command}} {{command_arguments}}`
