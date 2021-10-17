# pssh

> Parallel SSH program.
> More information: <https://manned.org/pssh>.

- Run a command on two hosts, and print its output on each server inline:

`pssh -i -H "{{host1}} {{host2}}" {{hostname -i}}`

- Run a command and save the output to separate files:

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{hostname -i}}`

- Run a command on multiple hosts, specified in a new-line separated file:

`pssh -i -h {{path/to/hosts_file}} {{hostname -i}}`

- Run a command as root (this asks for the root password):

`pssh -i -h {{path/to/hosts_file}} -A -l {{root_username}} {{hostname -i}}`

- Run a command with extra SSH arguments:

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{hostname -i}}`

- Run a command limiting the number of parallel connections to 10:

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
