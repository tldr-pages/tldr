# lslocks

> List local system locks.

- List all local system locks:

`lslocks`

- List locks with defined column headers:

`lslocks --output {{PID}},{{COMMAND}},{{PATH}}`

- List locks producing a raw output (no columns), and without column headers:

`lslocks --raw --noheadings`

- List locks by PID input:

`lslocks --pid {{PID}}`

- List locks with json output to `stdout`:

`lslocks --json`
