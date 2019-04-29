# nsenter

> Run a new command in a running process' namespace.

- Run command in existing processes network namespace:

`nsenter -t {{pid}} -n {{command}}`
