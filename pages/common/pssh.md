# pssh

> Parallel ssh program.

- Run a command on host1 and host2 to print the date on each server inline:

`pssh -i -H "{{host1}} {{host2}}" {{date}}`

- Run a command and save the output to separate files:

`pssh -H {{host1}} -H {{host2}} -o {{path/to/output_dir}} {{date}}`

- Run a command on each host specified in a new-line separated host file:

`pssh -i -h {{path/to/hosts_file}} {{date}}`

- Run a command as root; asks for root password:

`pssh -i -h {{path/to/hosts_file}} -A -l {{root}} {{date}}`

- Run a command with extra SSH arguments:

`pssh -i -h {{path/to/hosts_file}} -x "{{-O VisualHostKey=yes}}" {{date}}`

- Run a command using a maximum number of concurrent connections:

`pssh -i -h {{path/to/hosts_file}} -p {{10}} '{{cd dir; ./script.sh; exit}}'`
