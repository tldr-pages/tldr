# usleep

> Delay execution for a specific interval in microseconds.
> Note: This command is deprecated, use `nanosleep` instead.
> See also: `sleep`.
> More information: <https://manned.org/usleep.1>.

- Delay in microseconds:

`usleep {{microseconds}}`

- Execute a specific command after a 500,000 microseconds delay:

`usleep 500000 && {{command}}`
