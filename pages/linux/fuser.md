# fuser

> Display process IDs currently using files or sockets.
> Requires admin privileges.

- Identify process using a TCP socket:

`fuser -n tcp {{port}}`

- Find which process accessing a directory:

`fuser {{path/to/directory}}`

- Kill and signal processes accessing a file:

`fuser -k {{path/to/file}}`

- Find which processes are accessing a file:

`fuser -m {{path/to/file}}`

- The verbose mode shows the fields USER, PID, ACCESS and COMMAND. The output is similar to ps:

`fuser -v`
