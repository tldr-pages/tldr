# sysctl

> List and change kernel runtime variables.
> More information: <https://manned.org/sysctl.8>.

- Show all available variables and their values:

`sysctl {{[-a|--all]}}`

- Set a changeable kernel state variable:

`sysctl {{[-w|--write]}} {{section.tunable}}={{value}}`

- Get currently open file handlers:

`sysctl fs.file-nr`

- Get limit for simultaneous open files:

`sysctl fs.file-max`

- Apply changes from `/etc/sysctl.conf`:

`sysctl {{[-p|--load]}}`
