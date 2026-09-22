# nx

> The Nexium compiler and its tools: build, run, test, format and ship Nexium programs.
> More information: <https://londopy.github.io/nexium/>.

- Build and run a program (arguments after `--` go to it):

`nx run {{path/to/file.nx}} -- {{argument1 argument2 ...}}`

- Run the `test` blocks of a file, again on every change:

`nx test {{path/to/file.nx}} --watch`

- Type-check without building, with warnings as errors:

`nx check {{path/to/file.nx}} --strict`

- Build an optimized binary:

`nx build {{path/to/file.nx}} --mode fast -o {{path/to/output}}`

- Show the effects of every function (`allocates`, `blocks`, `panics`, ...):

`nx effects {{path/to/file.nx}}`

- Format sources in place, or only report the ones that would change:

`nx fmt {{path/to/file1.nx path/to/file2.nx ...}} --check`

- Produce the artifacts a file declares (a C library, a Python wheel, a Rust crate, an npm package):

`nx ship {{path/to/file.nx}}`

- Start an interactive session:

`nx repl`
