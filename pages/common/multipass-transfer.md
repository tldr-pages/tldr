# multipass transfer

> Transfer files between the host and the virtual machine.
> Relative paths on instance start from home folder (just like scp).
> More information: <https://canonical.com/multipass/docs/latest/reference/command-line-interface/transfer/>.

- Transfer a file host to instance:

`multipass transfer {{path/to/local_file}} {{instance_name}}:{{path/to/remote_directory}}`

- Transfer a file from an instance to host:

`multipass transfer {{instance_name}}:{{path/to/remote_file}} {{path/to/local_directory}}`

- Transfer a directory from your local machine to an instance:

`multipass transfer -r {{path/to/local_directory}} {{instance_name}}:{{path/to/remote_directory}}`
