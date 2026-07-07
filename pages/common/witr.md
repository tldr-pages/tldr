# witr

> Inspect processes, services, and ports by tracing their origin.
> More information: <https://github.com/pranshuparmar/witr>.

- Inspect a process by name:

`witr {{process-name}}`

- Inspect a process by PID:

`witr --pid {{pid}}`

- Find which process is using a network port:

`witr --port {{port}}`

- Show full process tree for a PID:

`witr --pid {{pid}} --tree`

- Show a short summary output:

`witr --short {{process-name}}`

- Display the results in a JSON format:

`witr --json --pid {{pid}}`
