# trace-cmd record

> Capture kernel trace events.
> See also: `trace-cmd list`, `trace-cmd report`.
> More information: <https://manned.org/trace-cmd-record>.

- Record a trace with a specific plugin:

`sudo trace-cmd record -p {{plugin}}`

- Record a trace of a specific executable:

`sudo trace-cmd record -F {{executable}}`

- Record a trace of a specific function:

`sudo trace-cmd record -g {{function}}`

- Exclude a specific function from the trace:

`sudo trace-cmd record -n {{function}}`

- Limit the function call graph depth:

`sudo trace-cmd record --max-graph-depth {{depth}}`

- Record a trace from a specific process ID:

`sudo trace-cmd record -P {{pid}}`
