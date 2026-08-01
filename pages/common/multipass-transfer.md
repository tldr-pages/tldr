# multipass transfer

> Transfer files between the host and the virtual machine.
> Note: Relative paths on an instance start from the user's home directory.
> More information: <https://canonical.com/multipass/docs/latest/reference/command-line-interface/transfer/>.

- Transfer a file from the host to an instance:

`multipass transfer {{path/to/local_file}} {{instance_name}}:{{path/to/remote_directory}}`

- Transfer a file from an instance to the host:

`multipass transfer {{instance_name}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer a directory from the host to an instance:

`multipass transfer {{[-r|--recursive]}} {{path/to/local_directory}} {{instance_name}}:{{path/to/remote_directory}}`
