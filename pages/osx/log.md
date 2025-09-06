# log

> View, export, and configure logging systems.
> More information: <https://keith.github.io/xcode-man-pages/log.1.html>.

- Stream live system logs:

`log stream`

- Stream logs sent to `syslog` from the process with a specific PID:

`log stream --process {{process_id}}`

- Show logs sent to syslog from a process with a specific name:

`log show --predicate "process == '{{process_name}}'"`

- Export all logs to disk for the past hour:

`sudo log collect --last {{1h}} --output {{path/to/file.logarchive}}`
