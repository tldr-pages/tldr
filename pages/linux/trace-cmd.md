# trace-cmd

> Utility to interact with the Ftrace Linux kernel internal tracer.
> See also: `trace-cmd-list`, `trace-cmd-record`, `trace-cmd-report`.
> More information: <https://manned.org/trace-cmd>.

- Display the status of tracing system:

`trace-cmd stat`

- List available tracers:

`trace-cmd list -t`

- Start tracing with a specific plugin:

`trace-cmd start -p {{plugin}}`

- View the trace output:

`trace-cmd show`

- Stop the tracing but retain the buffers:

`trace-cmd stop`

- Clear the trace buffers:

`trace-cmd clear`

- Record a trace:

`trace-cmd record`

- Display the recorded trace:

`trace-cmd report`
