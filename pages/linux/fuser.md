# fuser

> Display process IDs currently using files or sockets.
> More information: <https://manned.org/fuser>.

- Find which processes are accessing a file or directory:

`fuser {{path/to/file_or_directory}}`

- Show more fields (`USER`, `PID`, `ACCESS` and `COMMAND`):

`fuser {{[-v|--verbose]}} {{path/to/file_or_directory}}`

- Identify processes using a TCP socket:

`fuser {{[-n|--namespace]}} tcp {{port}}`

- Kill all processes accessing a file or directory (sends the `SIGKILL` signal):

`fuser {{[-k|--kill]}} {{path/to/file_or_directory}}`

- Find which processes are accessing the filesystem containing a specific file or directory:

`fuser {{[-m|--mount]}} {{path/to/file_or_directory}}`

- Kill all processes with a TCP connection on a specific port:

`fuser {{[-k|--kill]}} {{port}}/tcp`
