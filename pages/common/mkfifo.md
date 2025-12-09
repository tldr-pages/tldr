# mkfifo

> Make named pipes, also known as First In First Out (FIFO).
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Create a named pipe at a given path:

`mkfifo {{path/to/pipe}}`

- Send data through a named pipe and send the command to the background:

`echo "{{Hello World}}" > {{path/to/pipe}} &`

- Receive data through a named pipe:

`cat {{path/to/pipe}}`

- Share your terminal session in real-time:

`mkfifo {{path/to/pipe}}; script {{[-f|--flush]}} {{path/to/pipe}}`
