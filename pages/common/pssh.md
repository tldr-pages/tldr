# pssh

> Parallel SSH program.

- Run a command on two hosts, and print its output on each server inline:

`pssh -i -H "{{host1}} {{host2}}" {{echo "foo"}}`

- Run a command and save the output to separate files:

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{echo "foo"}}`

- Run a command on multiple hosts, specified in a new-line separated file:

`pssh -i -h {{path/to/hosts_file}} {{echo "foo"}}`

- Run a command as root (this asks for the root password):

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{echo "foo"}}`

- Run a command with extra SSH arguments:

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{echo "foo"}}`

- Run a command using the maximum number of concurrent connections:

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
