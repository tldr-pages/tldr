# strip

> Discard symbols from executables or object files.
> More information: <https://manned.org/strip>.

- Replace the input file with its stripped version:

`strip {{path/to/file}}`

- Put the stripped output in file, rather than replacing the existing one:

`strip {{path/to/input_file}} -o {{path/to/output_file}}`

- Strip debug symbols only:

`strip --strip-debug {{/path/to/file.o}}`
