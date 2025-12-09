# fatrace

> Report file access events.
> More information: <https://manned.org/fatrace>.

- Print file access events in all mounted filesystems to `stdout`:

`sudo fatrace`

- Print file access events on the mount of the current directory, with timestamps, to `stdout`:

`sudo fatrace {{[-c|--current-mount]}} {{[-t|--timestamp]}}`
