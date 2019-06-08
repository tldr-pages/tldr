# dep

> Tool for dependency management in Go projects.
> More information: <https://golang.github.io/dep>.

- Initialize the current directory as the root of a Go project:

`dep init`

- Install any missing dependencies (Scans Gopkg.toml and your .go files):

`dep ensure`

- Report the status of the project's dependencies:

`dep status`

- Add a dependency to the project:

`dep ensure -add {{package_url}}`

- Update the locked versions of all dependencies:

`dep ensure -update`
