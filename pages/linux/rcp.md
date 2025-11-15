# rcp

> Copy files between local and remote systems.
> It mimics the behavior of the `cp` command but operates across different machines.
> More information: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rcp-invocation>.

- Copy a file to a remote host:

`rcp {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- Copy a directory recursively:

`rcp {{[-r|--recursive]}} {{path/to/local_directory}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- Preserve the file attributes:

`rcp {{[-p|--preserve]}} {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`

- Force copy without a confirmation:

`rcp {{[-f|--from]}} {{path/to/local_file}} {{username}}@{{remote_host}}:/{{path/to/destination}}/`
