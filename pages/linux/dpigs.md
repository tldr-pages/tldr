# dpigs

> Show which installed packages occupy the most space.
> Sorts the installed packages by size and outputs the largest ones.
> More information: <https://manned.org/man/dpigs>.

- OPTIONS:

`-n, --lines=N`
`Display the N largest packages on the system (default 10).`

`-s, --status=FILE`
`Use FILE instead of the default dpkg status file (which is /var/lib/dpkg/status currently).`

`-S, --source`
`Display the largest source packages of binary packages installed on the system.`

`-H, --human-readable`
`Display package sizes in human-readable format (like ls -lh or du -h)`

`-h, --help`
`Display some usage information and exit.`
