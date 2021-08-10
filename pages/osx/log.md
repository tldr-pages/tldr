# log

> View, export, and configure logging systems.
> More information: <https://www.dssw.co.uk/reference/log.html>.

- Stream live system logs:

`log stream`

- Stream logs sent to syslog from the process with a specific PID:

`log stream --process {{235}}`

- Show logs sent to syslog for process named 'dasd':

`log show --predicate "process == '{{dasd}}'"`

- Dump all logs for the past hour:

`sudo log collect --last {{1h}}`
