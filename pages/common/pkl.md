# pkl

> Manages, evaluates, and tests Pkl configuration modules.
> More information: <https://pkl-lang.org/main/current/pkl-cli>.

- Evaluate the given Pkl modules and produce their rendering results:

`pkl eval {{module.pkl}}`

- Run as a server that communicates over `stdin` and `stdout`:

`pkl server`

- Evaluate Pkl modules as tests and produces a report:

`pkl test {{module.pkl}}`

- Start a REPL session:

`pkl repl`

- Prepare a Pkl project for publishing as a package:

`pkl project package {{path/to/project_directory}}`

- Resolve project dependencies and writes the resolved versions to a file at path `PklProject.deps.json`:

`pkl project resolve {{path/to/project_directory}}`
