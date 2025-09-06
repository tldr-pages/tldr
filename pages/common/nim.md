# nim

> The Nim compiler.
> Processes, compiles and links Nim language source files.
> More information: <https://nim-lang.org/docs/nimc.html>.

- Compile a source file:

`nim {{[c|compile]}} {{path/to/file.nim}}`

- Compile and run a source file:

`nim {{[c|compile]}} {{[-r|--run]}} {{path/to/file.nim}}`

- Compile a source file with release optimizations enabled:

`nim {{[c|compile]}} {{[-d|--define]}}:release {{path/to/file.nim}}`

- Build a release binary optimized for low file size:

`nim {{[c|compile]}} {{[-d|--define]}}:release --opt:size {{path/to/file.nim}}`

- Generate HTML documentation for a module (output will be placed in the current directory):

`nim doc {{path/to/file.nim}}`

- Check a file for syntax and semantics:

`nim check {{path/to/file.nim}}`
