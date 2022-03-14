# pmap

> Report memory map of a process or processes.
> More information: <https://manned.org/pmap>.

- Print memory map for a process selected by its process id (PID).

`pmap {{pid}}`

- Show the extended format.

`pmap -x {{pid}}`

- Show the device format.

`pmap -d {{pid}}`

- Limit results to a memory address range specified by _low_ and _high_.

`pmap -A {{low}},{{high}}`
