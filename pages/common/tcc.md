# tcc

> A tiny C compiler that can run C source files as scripts and otherwise has command line options similar to `gcc`.
> More information: <https://bellard.org/tcc/tcc-doc.html>.

- Compile and link `a.c` and `b.c` to generate an executable:

`tcc -o {{executable_name}} {{path/to/a.c}} {{path/to/b.c}}`

- Directly run `a.c` like a script and pass arguments to it:

`tcc -run {{path/to/a.c}} {{arguments}}`

- Interpret C source files with a shebang inside the file:

`#!/full/path/to/tcc -run`
