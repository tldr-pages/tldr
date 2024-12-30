# numactl

> 控制进程或共享内存的 NUMA 策略。
> 更多信息：<https://manned.org/numactl>。

- 在节点 0 上运行命令，并在节点 0 和 1 上分配内存：

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{command}} {{command_arguments}}`

- 在当前 cpuset 的 CPU（核心） 0-4 和 8-12 上运行命令：

`numactl --physcpubind={{+0-4,8-12}} -- {{command}} {{command_arguments}}`

- 在所有 CPU 上以交错方式运行命令：

`numactl --interleave={{all}} -- {{command}} {{command_arguments}}`