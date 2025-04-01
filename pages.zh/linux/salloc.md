# salloc

> 在集群中分配一个或多个节点，以启动交互式 shell 会话或执行命令。
> 更多信息：<https://slurm.schedmd.com/salloc.html>.

- 在集群中的节点上启动交互式 shell 会话：

`salloc`

- 在集群中的节点上同步执行指定的命令：

`salloc {{ls -a}}`

- 仅分配满足指定约束条件的节点：

`salloc --constraint={{(amd|intel)&gpu}}`
