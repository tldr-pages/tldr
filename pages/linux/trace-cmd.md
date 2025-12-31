# trace-cmd

> Utility to interact with the Ftrace Linux kernel internal tracer.
> See also: `trace-cmd list`, `trace-cmd record`, `trace-cmd report`.
> More information: <https://manned.org/trace-cmd>.

- Display the status of tracing system:

`sudo trace-cmd stat`

- List available tracers:

`sudo trace-cmd list -t`

- Start tracing with a specific plugin:

`sudo trace-cmd start -p {{function|function_graph|preemptirqsoff|irqsoff|preemptoff|wakeup|...}}`

- View the trace output:

`sudo trace-cmd show`

- Stop the tracing but retain the buffers:

`sudo trace-cmd stop`

- Clear the trace buffers:

`sudo trace-cmd clear`

- Record a trace:

`sudo trace-cmd record`

- Display the recorded trace:

`sudo trace-cmd report`
