# numactl

> Control NUMA policy for processes or shared memory.
> More information: <https://man7.org/linux/man-pages/man8/numactl.8.html>.

- Run a command on node 0 with memory allocated on node 0 and 1:

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{command}} {{command_arguments}}`

- Run a command on CPUs (cores) 0-4 and 8-12 of the current cpuset:

`numactl --physcpubind={{+0-4,8-12}} -- {{command}} {{command_arguments}}`

- Run a command with its memory interleaved on all CPUs:

`numactl --interleave={{all}} -- {{command}} {{command_arguments}}`
