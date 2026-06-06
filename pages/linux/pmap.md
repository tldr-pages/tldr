# pmap

> Report memory map of a process or processes.
> More information: <https://manned.org/pmap>.

- Print memory map for a specific process ID (PID):

`pmap {{process_id}}`

- Show the extended format:

`pmap --extended {{process_id}}`

- Show the device format:

`pmap --device {{process_id}}`

- Limit results to a memory address range specified by `low` and `high`:

`pmap --range {{low}},{{high}}`

- Print memory maps for multiple processes:

`pmap {{pid1 pid2 ...}}`
