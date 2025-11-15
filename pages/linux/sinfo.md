# sinfo

> View information about Slurm nodes and partitions.
> See also: `squeue`, `sbatch`, which are also part of the Slurm workload manager.
> More information: <https://slurm.schedmd.com/sinfo.html>.

- Show a quick summary overview of the cluster:

`sinfo {{[-s|--summarize]}}`

- View the detailed status of all partitions across the entire cluster:

`sinfo`

- View the detailed status of a specific partition:

`sinfo {{[-p|--partition]}} {{partition_name}}`

- View information about idle nodes:

`sinfo {{[-t|--states]}} {{idle}}`

- Summarise dead nodes:

`sinfo {{[-d|--dead]}}`

- List dead nodes and the reasons why:

`sinfo {{[-R|--list-reasons]}}`
