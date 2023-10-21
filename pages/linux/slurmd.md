# slurmd

> Monitors all tasks running on the compute node, accepts tasks, launches tasks, and kills running tasks upon request.
> More information: <https://slurm.schedmd.com/slurmd.html>.

- Report node rebooted when daemon restarted (Used for testing purposes):

`slurmd -b`

- Run the daemon with the given nodename:

`slurmd -N {{nodename}}`

- Write log messages to the specified file:

`slurmd -L {{path/to/output_file}}`

- Read configuration from the specified file:

`slurmd -f {{path/to/file}}`

- Display help:

`slurmd -h`
