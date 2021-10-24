# for

> Shell loop over parameters.
> More information: <https://man.archlinux.org/man/for.n>.

- Perform a command with different arguments:

`for argument in 1 2 3; do {{command $argument}}; done`

- Perform a command in every directory:

`for d in *; do (cd $d; {{command}}); done`
