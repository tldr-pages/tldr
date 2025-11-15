# hatch

> Modern, extensible Python project manager.
> See also: `poetry`.
> More information: <https://hatch.pypa.io/latest/cli/reference/>.

- Create a new Hatch project:

`hatch new {{project_name}}`

- Initialize Hatch for an existing project:

`hatch new --init`

- Build a Hatch project:

`hatch build`

- Remove build artifacts:

`hatch clean`

- Create a default environment with dependencies defined in the `pyproject.toml` file:

`hatch env create`

- Show environment dependencies as a table:

`hatch dep show table`
