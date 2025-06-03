# uv init

> Create a new project.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-init>.

- Initialize a project in the current directory:

`uv init`

- Initialize a project with a certain name:

`uv init {{project_name}}`

- Create a project for a Python library:

`uv init --lib {{project_name}}`

- Specify the build system:

`uv init --build-backend {{build_backend}} {{project_name}}`

- Only create a `pyproject.toml`:

`uv init --bare {{project_name}}`

- Set the project description:

`uv init --description "{{description}}" {{project_name}}`
