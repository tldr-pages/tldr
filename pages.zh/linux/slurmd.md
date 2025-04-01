# slurmd

> 监视计算节点上运行的所有任务，接受任务，启动任务，并根据请求终止运行中的任务。
> 更多信息：<https://slurm.schedmd.com/slurmd.html>.

- 当守护进程重启时报告节点重启（用于测试目的）：

`slurmd -b`

- 使用给定的节点名称运行守护进程：

`slurmd -N {{nodename}}`

- 将日志消息写入指定文件：

`slurmd -L {{path/to/output_file}}`

- 从指定文件读取配置：

`slurmd -f {{path/to/file}}`

- 显示帮助：

`slurmd -h`
