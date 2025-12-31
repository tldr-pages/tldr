# salloc

> Start an interactive shell session or execute a command by allocating one or more nodes in a cluster.
> More information: <https://slurm.schedmd.com/salloc.html>.

- Start an interactive shell session on a node in the cluster:

`salloc`

- Execute the specified command synchronously on a node in the cluster:

`salloc {{ls --all}}`

- Only allocate nodes fulfilling the specified constraints:

`salloc {{[-C|--constraint]}} {{(amd|intel)&gpu}}`
