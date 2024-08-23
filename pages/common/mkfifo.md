# mkfifo

> Make FIFOs (named pipes).
> More information: <https://www.gnu.org/software/coreutils/mkfifo>.

- Create a named pipe at a given path:

`mkfifo {{path/to/pipe}}`

- Send data through a named pipe and send the command to the background:

`echo {{"Hello World"}} > {{path/to/pipe}} &`

- Receive data through a named pipe:

`cat {{path/to/pipe}}`
