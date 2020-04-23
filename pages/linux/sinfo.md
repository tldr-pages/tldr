# sinfo

> View information about Slurm nodes and partitions.
> See also `squeue` and `sbatch`, which are also part of the Slurm workload manager.
> More information: <https://slurm.schedmd.com/sinfo.html>.

- Show a quick summary overview of the cluster:

`sinfo --summarize`

- View the detailed status of all partitions across the entire cluster:

`sinfo`

- View the detailed status of a specific partition:

`sinfo --partition {{partition_name}}`

- View information about idle nodes:

`sinfo --states {{idle}}`

- Summarise dead nodes:

`sinfo --dead`

- List dead nodes and the reasons why:

`sinfo --list-reasons`
