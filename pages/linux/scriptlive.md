# scriptlive

> Execute a typescript created by the `script` command in real-time.
> See also: `script`.
> More information: <https://manned.org/scriptlive>.

- Execute a typescript in real-time:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}}`

- Execute a typescript at double the original speed:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --divisor 2`

- Execute a typescript created using `--log-in` option of `script`:

`scriptlive --log-in {{path/to/stdin_log_file}} {{path/to/typescript}}`

- Execute a typescript waiting at most 2 seconds between each command:

`scriptlive {{path/to/timing_file}} {{path/to/typescript}} --maxdelay 2`
