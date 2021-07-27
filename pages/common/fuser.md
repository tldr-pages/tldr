# fuser

> Identify processes using files or sockets.
> More information: <https://manned.org/fuser>.

- Identify processes using a file:

`fuser {{path/to/file}}`

- Identify processes using a file displaying a verbose output:

`fuser --verbose {{path/to/file}}`

- Identify the process using socket on TCP port 8080:

`fuser tcp/8080`

- Kill processes using socket on TCP port 8080:

`fuser --kill tcp/8080`