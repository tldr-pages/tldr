# salloc

> 通过在集群中分配一个或多个节点来启动一个交互式 shell 会话或执行一个命令。
> 更多信息：<https://slurm.schedmd.com/salloc.html>。

- 在集群中的节点上启动一个交互式 shell 会话：

`salloc`

- 在集群中的节点上同步执行指定的命令：

`salloc {{ls -a}}`

- 仅分配满足指定约束的节点：

`salloc --constraint={{(amd|intel)&gpu}}`