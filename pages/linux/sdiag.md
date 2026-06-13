# sdiag

> Show information about the execution of `slurmctld`.
> More information: <https://slurm.schedmd.com/sdiag.html>.

- Show all performance counters related to the execution of `slurmctld`:

`sdiag {{[-a|--all]}}`

- Reset performance counters related to the execution of `slurmctld`:

`sdiag {{[-r|--reset]}}`

- Specify the output format:

`sdiag {{[-a|--all]}} --{{json|yaml}}`

- Specify the cluster to send commands to:

`sdiag {{[-a|--all]}} {{[-M|--cluster]}} {{cluster_name}}`
