# slurmctld

> Monitor all other Slurm daemons and resources, accept work (jobs), and allocate resources to those jobs.
> More information: <https://slurm.schedmd.com/slurmctld.html>.

- Clear all previous slurmctld state from its last checkpoint:

`slurmctld -c`

- Print a brief summary of command options:

`slurmctld -h`

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmctld -n {{value}}`

- Write log messages to the specified file:

`slurmctld -L {{file}}`

- Print version information and exit:

`slurmctld -V`
