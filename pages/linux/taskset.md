# taskset

> Get or set a process' CPU affinity or start a new process with a defined CPU affinity.
> More information: <https://manned.org/taskset>.

- Get a running process' CPU affinity by PID:

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{pid}}`

- Set a running process' CPU affinity by PID:

`taskset {{[-p|--pid]}} {{[-c|--cpu-list]}} {{cpu_id}} {{pid}}`

- Start a new process with affinity for a single CPU:

`taskset {{[-c|--cpu-list]}} {{cpu_id}} {{command}}`

- Start a new process with affinity for multiple non-sequential CPUs:

`taskset {{[-c|--cpu-list]}} {{cpu_id_1,cpu_id_2,cpu_id_3,...}}`

- Start a new process with affinity for CPUs 1 through 4:

`taskset {{[-c|--cpu-list]}} {{cpu_id_1}}-{{cpu_id_4}}`
