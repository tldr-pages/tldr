# slurmctld

> Monitor all other Slurm daemons and resources, accept work (jobs), and allocate resources to those jobs.
> More information: <https://slurm.schedmd.com/slurmctld.html>.

- Clear all previous `slurmctld` states from its last checkpoint:

`slurmctld -c`

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmctld -n {{value}}`

- Write log messages to the specified file:

`slurmctld -L {{path/to/output_file}}`

- Display help:

`slurmctld -h`

- Display version:

`slurmctld -V`
