# fatrace

> Report file access events.
> See also: `inotifywait`.
> More information: <https://manned.org/fatrace>.

- Print file access events in all mounted filesystems to `stdout`:

`sudo fatrace`

- Limit output to a program with a specific name:

`sudo fatrace {{[-C|--command]}} {{program_name}}`

- Print file access events on the mount of the current directory to `stdout`:

`sudo fatrace {{[-c|--current-mount]}}`

- Add timestamps to the printout:

`sudo fatrace {{[-t|--timestamp]}}`
