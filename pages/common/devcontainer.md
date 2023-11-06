# devcontainer

> Use a Docker container as a development environment.
> More information: <https://containers.dev/>.

- Create and run a Dev Container:

`devcontainer up`

- Apply a Dev Container Template to a workspace:

`devcontainer templates apply --template-id {{template_id}} --template-args {{template_args}} --workspace-folder {{path/to/workspace}}`

- Execute a command on a running Dev Container in the current workspace:

`devcontainer exec {{command}}`

- Build a Dev Container image from `devcontainer.json`:

`devcontainer build {{path/to/workspace}}`

- Open a Dev Container in VS Code (the path is optional):

`devcontainer open {{path/to/workspace}}`

- Read and print the configuration of a Dev Container from `devcontainer.json`:

`devcontainer read-configuration`
