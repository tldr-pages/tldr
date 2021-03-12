# coredumpctl

> Retrieve and process saved core dumps and metadata.
> More information: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- List all captured core dumps:

`coredumpctl list`

- List captured core dumps for a program:

`coredumpctl list {{program}}`

- Show information about the core dumps matching a program with `PID`:

`coredumpctl info {{PID}}`

- Invoke debugger using the last core dump of a program:

`coredumpctl debug {{program}}`

- Extract the last core dump of a program to a file:

`coredumpctl --output={{path/to/file}} dump {{program}}`
