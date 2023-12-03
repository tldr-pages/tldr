# salloc

> Allocate nodes in a cluster and start an interactive shell session or execute a command.
> More information: <https://slurm.schedmd.com/salloc.html>.

- Start an interactive shell session on a node in the cluster:

`salloc`

- Execute the specified command synchroneously on a node in the cluster:

`salloc {{ls -a}}`

- Only allocate nodes fulfiling the specified constraints:

`salloc --constraint={{(amd|intel)&gpu}}`
