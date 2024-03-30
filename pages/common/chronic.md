# chronic

> Display `stdout` and `stderr` of a command if and only if it fails.
> More information: <https://joeyh.name/code/moreutils/>.

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-zero exit code or crashes:

`chronic {{command options ...}}`

- Display `stdout` and `stderr` of the specified command if and only if it produces a non-empty `stderr`:

`chronic -e {{command options ...}}`

- Enable [v]erbose mode:

`chronic -v {{command options ...}}`
