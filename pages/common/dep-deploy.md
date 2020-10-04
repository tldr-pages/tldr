# dep deploy

> A cli tool for deployment of PHP applications.
> More information: <https://deployer.org>.

- Initialize deployer in a project, may use a framework recipe template:

`dep init [-t Template]`

- Deploy an application to remote host:

`dep deploy [{{hostname}}]`

- Rollback to the previous working release:

`dep rollback`

- Connect to host through ssh:

`dep ssh [{{hostname}}]`

- List commands:

`dep list`

- Run any arbitrary command on hosts:

`dep run [{{host}}]`

- Display help for a command:

`dep help {{command}}`
