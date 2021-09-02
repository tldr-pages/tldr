# carp

> REPL and build tool for Carp.
> More information: <https://carp-lang.github.io/carp-docs/Manual.html>.

- Start a REPL:

`carp`

- Start a REPL with a custom prompt:

`carp --prompt "> "`

- Build a file:

`carp -b {{path/to/file.carp}}`

- Build and run a file:

`carp -x {{path/to/file.carp}}`

- Build a file with optimizations:

`carp -b --optimize {{path/to/file.carp}}`

- Transpile a file to C code:

`carp --generate-only {{path/to/file.carp}}`
