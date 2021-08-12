# numactl

> Control politica NUMA pentru procese sau memorie partajată.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/numactl.8.html>

- Rulați o comandă pe nodul 0 cu memorie alocată pe nodul 0 și 1:

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{command}} {{command_arguments}}`

- Rulați o comandă pe procesoare (nuclee) 0-4 și 8-12 ale cpusetului curent:

`numactl --physcpubind={{+0-4,8-12}} -- {{command}} {{command_arguments}}`

- Rulați o comandă cu memoria intercalată pe toate procesoarele:

`numactl --interleave={{all}} -- {{command}} {{command_arguments}}`
