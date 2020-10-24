# fuser

> Display process IDs currently using files or sockets.

- Find which processes are accessing a file or directory:

`fuser {{path/to/file_or_directory}}`

- Show more fields (`USER`, `PID`, `ACCESS` and `COMMAND`):

`fuser --verbose {{path/to/file_or_directory}}`

- Identify processes using a TCP socket:

`fuser --namespace tcp {{port}}`

- Kill all processes accessing a file or directory (sends the `SIGKILL` signal):

`fuser --kill {{path/to/file_or_directory}}`

- Find which processes are accessing the filesystem containing a specific file or directory:

`fuser --mount {{path/to/file_or_directory}}`
