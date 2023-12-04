# rcp

> Copy files between local and remote systems.
> It mimics the behavior of the `cp` command but operates across different machines.
> More information: <https://www.gnu.org/software/inetutils/manual/html_node/rcp-invocation.html>.

- Copy a file to a remote host:

`rcp {{path/to/local_file}} {{username}}@{{remotehost}}:{{/path/to/destination/}}`

- Copy a directory recursively:

`rcp -r {{path/to/local_directory}} {{username}}@{{remotehost}}:{{/path/to/destination/}}`

- Preserve the file attributes:

`rcp -p {{path/to/local_file}} {{username}}@{{remotehost}}:{{/path/to/destination/}}`

- Force copy without a confirmation:

`rcp -f {{path/to/local_file}} {{username}}@{{remotehost}}:{{/path/to/destination/}}`
