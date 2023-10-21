# slurmdbd

> provides a secure enterprise-wide interface to a database for Slurm.
> More information: <https://slurm.schedmd.com/slurmdbd.html>.

- print a brief summary of command options:

`slurmdbd -h`

- Set the daemon's nice value to the specified value, typically a negative number:

`slurmdbd -n {{value}}`

- Change working directory of slurmdbd to LogFile path if possible, or to /var/tmp otherwise:

`slurmdbd -s`

- Print version information and exit:

`slurmdbd -V`