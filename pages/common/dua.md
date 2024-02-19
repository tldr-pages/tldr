# dua

> Dua (Disk Usage Analyzer): get the disk space usage of a directory.
> More information: <https://github.com/Byron/dua-cli>.

- Analyze specific directory:

`dua {{path/to/directory}}`

- Display apparent size instead of disk usage:

`dua --apparent-size`

- Count hard-linked files each time they are seen:

`dua --count-hard-links`

- Aggregate the consumed space of one or more directories or files:

`dua aggregate`

- Launch the terminal user interface:

`dua interactive`

- Format printing byte counts:

`dua --format {{metric|binary|bytes|GB|GiB|MB|MiB}}`

- Use a specific number of threads (defaults to the process number of threads):

`dua --threads {{count}}`
