# guile

> Guile Scheme interpreter.

- Start the Guile Scheme REPL:

`guile`

- Execute script in a given Scheme file:

`guile {{script.scm}}`

- Execute a Scheme expression:

`guile -c "{{expression}}"`

- Listen on a port or socket (if the port argument is unspecified, the default is port 37146) for remote REPL connections:

`guile --listen={{port_or_socket}}`
