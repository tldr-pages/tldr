# pkl

> Command line interface for `Pkl`, an embedded configuration language with rich support for validation and tooling.
> More information: <https://pkl-lang.org/main/current/pkl-cli>.

- Evaluate the given Pkl <modules> and produce their rendering results:

`pkl eval [<options>] [<modules>]`

- Run as a server that communicates over standard input/output:

`pkl server`

- Evaluate Pkl modules as tests and produces a report:

`pkl test [<options>] [<modules>]`

- Start a **REPL** session:

`pkl repl`

- Prepare a Pkl project for publishing as a package:

`pkl project package <project-dir>`

- Resolve project dependencies and writes the resolved versions to a file at path `PklProject.deps.json`:

`pkl project resolve <project-dir>`
