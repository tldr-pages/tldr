# for

> Shell bucla peste parametri.
> Mai multe informaţii: <https://man.archlinux.org/man/for.n>

- Efectuați o comandă cu diferite argumente:

`for argument in 1 2 3; do {{command $argument}}; done`

- Efectuați o comandă în fiecare director:

`for d in *; do (cd $d; {{command}}); done`
