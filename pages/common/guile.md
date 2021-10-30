# guile

> Guile Scheme interpreter.
> More information: <https://www.gnu.org/software/guile>.

- Start a REPL (interactive shell):

`guile`

- Execute the script in a given Scheme file:

`guile {{script.scm}}`

- Execute a Scheme expression:

`guile -c "{{expression}}"`

- Listen on a port or a Unix domain socket (the default is port 37146) for remote REPL connections:

`guile --listen={{port_or_socket}}`
