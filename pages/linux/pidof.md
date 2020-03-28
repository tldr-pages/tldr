# pidof

> Gets the id of a process using it's name.

- List all process ids with given name:

`pidof {{bash}}`

- List a single process id with given name:

`pidof -s {{bash}}`

- List process ids including scripts with given name:

`pidof -x {{script.py}}`

- Kill all processes with given name:

``kill `pidof {{name}}` ``
