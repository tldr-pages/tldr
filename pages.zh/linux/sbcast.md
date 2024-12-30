# sbcast

> 将文件发送到作业分配的节点。
> 此命令仅应在 Slurm 批处理作业中使用。
> 更多信息：<https://slurm.schedmd.com/sbcast.html>。

- 将文件发送到当前作业分配的所有节点：

`sbcast {{path/to/file}} {{path/to/destination}}`

- 自动检测传输文件所依赖的共享库，并一同传输它们：

`sbcast --send-libs={{yes}} {{path/to/executable}} {{path/to/destination}}`