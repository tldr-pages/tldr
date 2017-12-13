# dep

> Tool for dependency management in the Go ecosystem.

- Initialize a directory to be a project:

`dep init`

- Install the project dependencies:

`dep ensure`

- Report the status of the project's depedencies:

`dep status`

- Add a new depedency:

`dep ensure -add {{project_url}}`

- Update the locked versions of all dependencies:

`dep ensure -update`
