# chronic

> Display `stdout` and `stderr` of a command if and only if it fails.
> More information: <https://manned.org/chronic>.

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-zero exit code or crashes:

`chronic {{command}} {{option1 option2 ...}}`

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-empty `stderr`:

`chronic -e {{command}} {{option1 option2 ...}}`

- Enable [v]erbose mode:

`chronic -v {{command}} {{option1 option2 ...}}`
