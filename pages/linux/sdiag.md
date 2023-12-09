# sdiag

> Show information about the execution of `slurmctld`.
> More information: <https://slurm.schedmd.com/sdiag.html>.

- Show all performance counters related to the execution of `slurmctld`:

`sdiag --all`

- Reset performance counters related to the execution of `slurmctld`:

`sdiag --reset`

- Specify the output format:

`sdiag --all --{{json|yaml}}`

- Specify the cluster to send commands to:

`sdiag --all --cluster={{cluster_name}}`
