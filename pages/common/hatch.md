# hatch

> Modern, extensible Python project manager.
> See also: `poetry`.
> More information: <https://hatch.pypa.io/latest/cli/reference/>.

- Create new Hatch project:

`hatch new {{project_name}}`

- Initialize Hatch for existing project:

`hatch new --init`

- Build Hatch project:

`hatch build`

- Remove build artifacts:

`hatch clean`

- Create default environment with dependencies defined in pyproject.toml:

`hatch env create`

- Show environment dependencies as table:

`hatch dep show table`
