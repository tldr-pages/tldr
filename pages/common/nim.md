# nim

> The Nim compiler.
> Processes, compiles and links Nim language source files.
> More information: <https://nim-lang.org/docs/nimc.html>.

- Compile a source file:

`nim compile {{path/to/file.nim}}`

- Compile and run a source file:

`nim compile -r {{path/to/file.nim}}`

- Compile a source file with release optimizations enabled:

`nim compile -d:release {{path/to/file.nim}}`

- Build a release binary optimized for low file size:

`nim compile -d:release --opt:size {{path/to/file.nim}}`

- Generate HTML documentation for a module (output will be placed in the current directory):

`nim doc {{path/to/file.nim}}`

- Check a file for syntax and semantics:

`nim check {{path/to/file.nim}}`
