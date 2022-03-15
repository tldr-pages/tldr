# sysctl

> List and change kernel runtime variables.
> More information: <https://manned.org/sysctl.8>.

- Show all available variables and their values:

`sysctl -a`

- Set a changeable kernel state variable:

`sysctl -w {{section.tunable}}={{value}}`

- Get currently open file handlers:

`sysctl fs.file-nr`

- Get limit for simultaneous open files:

`sysctl fs.file-max`

- Apply changes from `/etc/sysctl.conf`:

`sysctl -p`
