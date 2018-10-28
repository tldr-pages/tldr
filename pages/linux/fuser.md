# fuser

> Display process IDs currently using files or sockets.
> Require admin privileges.

- Identify process using a TCP socket:

`fuser -n tcp {{port}}`

- Find which process accessing a directory:

`fuser {{path_to_dir}}`

- Killing and signalling processes:

`fuser -k {{path_to_dir}}`

- Find which process is accessing a file:

`fuser -m {{path_to_dir}}`

- Verbose mode:

`fuser -v`
