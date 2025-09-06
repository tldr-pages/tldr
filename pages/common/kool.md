# kool

> Build software development environments.
> More information: <https://kool.dev/docs/>.

- Create a project using a specific preset:

`kool create {{preset}} {{project_name}}`

- Run a specific script defined in the `kool.yml` file in the current directory:

`kool run {{script}}`

- Start/stop services in the current directory:

`kool {{start|stop}}`

- Display status of the services in the current directory:

`kool status`

- Update to the latest version:

`kool self-update`

- Print the completion script for the specified shell:

`kool completion {{bash|fish|powershell|zsh}}`
