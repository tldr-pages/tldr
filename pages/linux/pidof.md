# pidof

> Gets the ID of a process using its name.
> More information: <https://manned.org/pidof>.

- List all process IDs with given name:

`pidof {{bash}}`

- List a single process ID with given name:

`pidof -s {{bash}}`

- List process IDs including scripts with given name:

`pidof -x {{script.py}}`

- Kill all processes with given name:

`kill $(pidof {{name}})`
