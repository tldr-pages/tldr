# dep

> Deploy PHP applications.
> Note: The Go command `dep` with the same name is deprecated and archived.
> More information: <https://deployer.org>.

- Interactively initialize deployer in the local path (use a framework template with `--template={{template}}`):

`dep init`

- Deploy an application to a remote host:

`dep deploy {{hostname}}`

- Rollback to the previous working release:

`dep rollback`

- Connect to a remote host via ssh:

`dep ssh {{hostname}}`

- List commands:

`dep list`

- Run any arbitrary command on the remote hosts:

`dep run "{{command}}"`

- Display help for a command:

`dep help {{command}}`
