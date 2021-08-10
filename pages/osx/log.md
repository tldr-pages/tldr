# log

> View, export, and configure logging systems.
> More information: <https://www.dssw.co.uk/reference/log.html>.

- Stream live system logs:

`log stream`

- Stream logs sent to syslog from the process with a specific PID:

`log stream --process {{235}}`

- Show logs sent to syslog from a process with a specific name:

`log show --predicate "process == '{{dasd}}'"`

- Export all logs to disk for the past hour:

`sudo log collect --last {{1h}}`
