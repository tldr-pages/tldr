# gprof

> Performance analysis tool for many programming languages.
> It profiles the function executions of a program.

- Compile binary with gprof information and run it to get {{gmon.out}}:

`gcc -pg {{program.c}} && {{./a.out}}`

- Run gprof to obtain profile output:

`gprof`

- Suppress profile fields' description:

`gprof -b`

- Display routines that have zero usage:

`gprof -bz`
