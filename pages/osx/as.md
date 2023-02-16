# as

> Portable GNU assembler.
> Primarily intended to assemble output from `gcc` to be used by `ld`.
> More information: <https://www.unix.com/man-page/osx/1/as/>.

- Assemble a file, writing the output to `a.out`:

`as {{path/to/file.s}}`

- Assemble the output to a given file:

`as {{path/to/file.s}} -o {{path/to/output_file.o}}`

- Generate output faster by skipping whitespace and comment preprocessing. (Should only be used for trusted compilers):

`as -f {{path/to/file.s}}`

- Include a given path to the list of directories to search for files specified in `.include` directives:

`as -I {{path/to/directory}} {{path/to/file.s}}`
