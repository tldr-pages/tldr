# bison

> GNU parser generator.
> More information: <https://manned.org/bison>.

- Compile a bison definition file:

`bison {{path/to/file.y}}`

- Compile in debug mode, which causes the resulting parser to write additional information to `stdout`:

`bison {{[-t|--debug]}} {{path/to/file.y}}`

- Specify the output filename:

`bison {{[-o|--output]}} {{path/to/output.c}} {{path/to/file.y}}`

- Be verbose when compiling:

`bison {{[-v|--verbose]}}`
