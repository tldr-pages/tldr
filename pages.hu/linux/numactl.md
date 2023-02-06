# numactl

> A folyamatok vagy a megosztott memória NUMA-politikájának vezérlése. További információ: <https://man7.org/linux/man-pages/man8/numactl.8.html>.

- Futtasson egy parancsot a 0. csomóponton a 0. és az 1. csomóponton kiosztott memóriával:

`numactl --cpunodebind={{0}} --membind={{0,1}} -- {{command}} {{command_arguments}}`

- Futtasson parancsot az aktuális cpuset 0-4 és 8-12 CPU-ján (magjain):

`numactl --physcpubind={{+0-4,8-12}} -- {{command}} {{command_arguments}}`

- Parancs futtatása az összes CPU-n elosztott memóriával:

`numactl --interleave={{all}} -- {{command}} {{command_arguments}}`
