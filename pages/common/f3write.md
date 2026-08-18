# f3write

> Fill a drive out with `.h2w` files to test its real capacity.
> See also: `f3read`, `f3probe`, `f3fix`.
> More information: <https://manned.org/f3write>.

- Write test files to a given directory, filling the drive:

`sudo f3write {{path/to/mount_point}}`

- Limit the write speed:

`sudo f3write {{[-w|--max-write-rate]}} {{kb_per_second}} {{path/to/mount_point}}`
