# guile

> Guile Scheme interpreter.

- Start the Guile Scheme REPL:

`guile`

- Execute the script in a given Scheme file:

`guile {{script.scm}}`

- Execute a Scheme expression:

`guile -c "{{expression}}"`

- Listen on a port or socket (the default port is 37146) for remote REPL connections:

`guile --listen={{port_or_socket}}`
