# numactl

> 控制进程或共享内存的NUMA策略。
> 更多信息：<https://manned.org/numactl>.

- 在节点0上运行命令，并在节点0和1上分配内存：

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{command}} {{command_arguments}}`

- 在当前cpuset的CPU（核心）0-4和8-12上运行命令：

`numactl --physcpubind={{+0-4,8-12}} -- {{command}} {{command_arguments}}`

- 以内存交错方式在所有CPU上运行命令：

`numactl --interleave={{all}} -- {{command}} {{command_arguments}}`
