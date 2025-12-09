# pssh

> Parallel SSH program.
> More information: <https://manned.org/pssh>.

- Run a command on two hosts, and print its output on each server inline:

`pssh {{[-i|--inline]}} {{[-H|--host]}} "{{host1}} {{host2}}" {{hostname --ip-addresses}}`

- Run a command and save the output to separate files:

`pssh {{[-H|--host]}} {{host1}} {{[-H|--host]}} {{host2}} {{[-o|--outdir]}} {{path/to/output_directory}} {{hostname --ip-addresses}}`

- Run a command on multiple hosts, specified in a new-line separated file:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{hostname --ip-addresses}}`

- Run a command as root (this asks for the root password):

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-A|--askpass]}} {{[-l|--user]}} {{root_username}} {{hostname --ip-addresses}}`

- Run a command with extra SSH arguments:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-x|--extra-arg]}} "{{-O VisualHostKey=yes}}" {{hostname --ip-addresses}}`

- Run a command limiting the number of parallel connections to 10:

`pssh {{[-i|--inline]}} {{[-h|--hosts]}} {{path/to/hosts_file}} {{[-p|-par]}} {{10}} '{{cd dir; ./script.sh; exit}}'`
