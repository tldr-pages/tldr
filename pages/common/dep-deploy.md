# dep

> A CLI tool for deployment of PHP applications.
> More information: <https://deployer.org>.

- Interactively initialize deployer in the local path (use a framework template with `--template={{template}}`):

`dep init`

- Deploy an application to remote host:

`dep deploy [{{hostname}}]`

- Rollback to the previous working release:

`dep rollback`

- Connect to host through ssh:

`dep ssh {{hostname}}`

- List commands:

`dep list`

- Run any arbitrary command on hosts:

`dep run "{{command}}"`

- Display help for a command:

`dep help {{command}}`
