# jobs

> 显示当前 shell 启动的进程信息的 shell 内置命令。
> 除 `-l` 和 `-p` 选项外，其他选项仅适用于 `bash`。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-jobs>.

- 查看当前 shell 启动的作业：

`jobs`

- 列出作业及其进程 ID：

`jobs -l`

- 显示状态已更改的作业信息：

`jobs -n`

- 仅显示进程 ID：

`jobs -p`

- 显示正在运行的进程：

`jobs -r`

- 显示已停止的进程：

`jobs -s`
