# coredumpctl

> Retrieve and process saved core dumps and metadata.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/coredumpctl.html>.

- List all captured core dumps:

`coredumpctl`

- List captured core dumps for a program:

`coredumpctl list {{program_name}}`

- Filter core dumps based on a specific signal:

`coredumpctl list COREDUMP_SIGNAL={{1..64}}`

- Show information about the core dumps matching a program with PID:

`coredumpctl info {{process_id}}`

- Invoke debugger using the last core dump:

`coredumpctl debug`

- Invoke debugger using the last core dump of a program:

`coredumpctl debug {{program_name}}`

- Extract the last core dump of a program to a file:

`coredumpctl dump {{program_name}} {{[-o|--output]}} {{path/to/file}}`

- Skip debuginfod and pagination prompts and then print the backtrace when using `gdb`:

`coredumpctl debug {{[-A|--debugger-arguments]}} "-iex 'set debuginfod enabled on' -iex 'set pagination off' -ex bt"`
