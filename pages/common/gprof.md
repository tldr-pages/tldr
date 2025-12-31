# gprof

> Performance analysis tool for many programming languages.
> It profiles the function executions of a program.
> More information: <https://ftp.gnu.org/old-gnu/Manuals/gprof/html_mono/gprof.html>.

- Compile binary to default `a.out` with gprof information and run it to get `gmon.out`:

`gcc {{[-p|-pg]}} {{program.c}} && ./a.out`

- Run gprof on default `a.out` and `gmon.out` to obtain profile output:

`gprof`

- Run gprof on a named binary:

`gprof {{path/to/binary}} {{path/to/gmon.out}}`

- Suppress profile field's description:

`gprof {{[-b|--brief]}}`

- Display routines that have zero usage:

`gprof {{[-bz|--brief --display-unused-functions]}}`
