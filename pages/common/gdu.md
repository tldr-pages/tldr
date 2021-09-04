# gdu

> Disk usage analyzer with console interface.
> More information: <https://github.com/dundee/gdu>.

- Show disk usage of the current directory:

`gdu`

- Show disk usage of given directory:

`gdu {{path/to/directory}}`

- Show disk usage of all mounted disks:

`gdu --show-disks`

- Show disk usage but ignore some paths:

`gdu --ignore-dirs {{/sys,/proc}} /`

- Ignore paths by regular pattern:

`gdu --ignore-dirs-pattern {{'.*[abc]+'}}`

- Ignore hidden directories:

`gdu --no-hidden`

- Only print result, do not enter interactive mode:

`gdu --non-interactive {{path/to/directory}}`

- Do not show progress in non-interactive mode, useful in scripts:

`gdu --no-progress {{path/to/directory}}`
