# coredumpctl

> Retrieve and process saved core dumps and metadata.
> More information: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- List all captured core dumps:

`coredumpctl`

- List captured core dumps for a program:

`coredumpctl list {{program}}`

- Show information about the core dumps matching a program with `PID`:

`coredumpctl info {{PID}}`

- Invoke debugger using the last core dump:

`coredumpctl debug`

- Invoke debugger using the last core dump of a program:

`coredumpctl debug {{program}}`

- Extract the last core dump of a program to a file:

`coredumpctl --output {{path/to/file}} dump {{program}}`

- Skip debuginfod and pagination prompts and then print the backtrace when using `gdb`:

`coredumpctl debug --debugger-arguments "-iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt"`
