# pmap

> Report memory map of a process.
> More information: <https://manned.org/pmap>.

- Print memory map for a specific process id (PID):

`pmap {{pid}}`

- Show the extended format:

`pmap --extended {{pid}}`

- Show the device format:

`pmap --device {{pid}}`

- Limit results to a memory address range specified by _low_ and _high_:

`pmap --range {{low}},{{high}}`
