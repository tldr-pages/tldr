# tcc

> A tiny C compiler that can run C source files as scripts and otherwise has command line options similar to gcc.
> More information: <https://bellard.org/tcc/tcc-doc.html>.

- Compile and link `a.c` and `b.c` to generate the executable `myprog`:

`tcc -o myprog a.c b.c`

- Directly run `a.c` like a script and pass `args` to it:

`tcc -run a.c args`

- Interpret C source files with a shebang inside the file:

`#!/full/path/to/tcc -run`
