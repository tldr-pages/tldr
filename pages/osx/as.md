# as

> Portable GNU assembler.
> Primarily intended to assemble output from `gcc` to be used by `ld`.

- Assemble a file, writing the output to `a.out`:

`as {{file.s}}`

- Assemble the output to a given file:

`as {{file.s}} -o {{out.o}}`

- Generate output faster by skipping whitespace and comment preprocessing. (Should only be used for trusted compilers):

`as -f {{file.s}}`

- Include a given path to the list of directories to search for files specified in `.include` directives:

`as -I {{path/to/directory}} {{file.s}}`
