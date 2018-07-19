# nim

> The Nim compiler.
> Processes, compiles and links Nim language source files.

- Compile a source file:

`nim compile {{file}}`

- Compile and run a source file:

`nim compile -r {{file}}`

- Compile a source file with release optimizations enabled:

`nim compile -d:release {{file}}`

- Build a release binary optimized for low file size:

`nim compile -d:release --opt:size {{file}}`

- Generate HTML documentation for a module:

`nim doc {{file}}`
