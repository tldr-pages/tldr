# fuser

> Display process IDs currently using files or sockets.
> Require admin privileges.

- Identify process using a TCP socket:

`fuser -n tcp {{port}}`

- Find which process accessing a directory:

`fuser {{path_to_dir}}`

- Kill and signal processes:

`fuser -k {{path_to_dir}}`

- Find which processes are accessing a file:

`fuser -m {{path_to_file}}`

- The verbose mode shows the fields USER, PID, ACCESS and COMMAND. The output is similar to ps:

`fuser -v`
