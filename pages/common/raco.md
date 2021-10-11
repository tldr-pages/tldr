# raco

> Racket command-line tools.
> More information: <https://docs.racket-lang.org/raco/>.

- List all available subcommands:

`raco help`

- Install a package, automatically installing dependencies:

`raco pkg install --auto {{package_source}}`

- Install the current directory as a package:

`raco pkg install`

- Build (or rebuild) bytecode, documentation, executables, and metadata indexes for a package:

`raco setup {{module/path/of/package}}`

- Run tests in a file:

`raco test {{path/to/source.rkt}}`
