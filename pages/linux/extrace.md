# extrace

> Trace exec() calls.
> More information: <https://github.com/chneukirchen/extrace>.

- Trace all program executions occurring on the system:

`sudo extrace`

- Run a command and only trace descendants of this command:

`sudo extrace {{command}}`

- Print the current working [d]irectory of each process:

`sudo extrace -d`

- Resolve the full path of each executable:

`sudo extrace -l`

- Display the [u]ser running each process:

`sudo extrace -u`
