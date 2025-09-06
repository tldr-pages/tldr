# lslocks

> List local system locks.
> More information: <https://manned.org/lslocks>.

- List all local system locks:

`lslocks`

- List locks with defined column headers:

`lslocks {{[-o|--output]}} {{PID}},{{COMMAND}},{{PATH}}`

- List locks producing a raw output (no columns), and without column headers:

`lslocks {{[-r|--raw]}} {{[-n|--noheadings]}}`

- List locks by PID input:

`lslocks {{[-p|--pid]}} {{PID}}`

- List locks with JSON output to `stdout`:

`lslocks {{[-J|--json]}}`
