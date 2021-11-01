# raco

> Racket command-line tools.
> More information: <https://docs.racket-lang.org/raco/>.

- Install a package, automatically installing dependencies:

`raco pkg install --auto {{package_source}}`

- Install the current directory as a package:

`raco pkg install`

- Build (or rebuild) bytecode, documentation, executables, and metadata indexes for collections:

`raco setup {{collection1 collection2 ...}}`

- Run tests in files:

`raco test {{path/to/tests1.rkt path/to/tests2.rkt ...}}`

- Search local documentation:

`raco docs {{search_terms ...}}`

- Display help:

`raco help`
