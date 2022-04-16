# pmap

> Report memory map of a process or processes.
> More information: <https://manned.org/pmap>.

- Print memory map for a specific process id (PID):

`pmap {{pid}}`

- Show the extended format:

`pmap --extended {{pid}}`

- Show the device format:

`pmap --device {{pid}}`

- Limit results to a memory address range specified by `low` and `high`:

`pmap --range {{low}},{{high}}`

- Print memory maps for multiple processes:

`pmap {{pid1 pid2 ...}}`
