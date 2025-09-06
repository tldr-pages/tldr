# sbcast

> Send a file to a job's allocated nodes.
> This command should only be used from within a Slurm batch job.
> More information: <https://slurm.schedmd.com/sbcast.html>.

- Send a file to all nodes allocated to the current job:

`sbcast {{path/to/file}} {{path/to/destination}}`

- Autodetect shared libraries the transmitted file depends upon and transmit them as well:

`sbcast --send-libs={{yes}} {{path/to/executable}} {{path/to/destination}}`
