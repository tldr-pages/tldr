# bison

> GNU parser generator.
> More information: <https://www.gnu.org/software/bison/>.

- Compile a bison definition file:

`bison {{path/to/file.y}}`

- Compile in debug mode, which causes the resulting parser to write additional information to `stdout`:

`bison --debug {{path/to/file.y}}`

- Specify the output filename:

`bison --output {{path/to/output.c}} {{path/to/file.y}}`

- Be verbose when compiling:

`bison --verbose`
