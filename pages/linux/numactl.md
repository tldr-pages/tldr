# numactl

> Control NUMA policy for processes or shared memory.

- Run command on node 0 with memory allocated on node 0 and 1:

`numactl --cpunodebind=0 --membind=0,1 {{command}}`

- Run command on CPUs (cores) 0-4 and 8-12 of the current cpu-set:

`numactl --physcpubind=+0-4,8-12 {{command}}`

- Run command with its memory interleaved on all CPUs:

`numactl --interleave=all {{command}}`
