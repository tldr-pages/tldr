# node

> Server-side JavaScript platform (Node.js).
> More information: <https://nodejs.org>.

- Run a JavaScript file:

`node {{path/to/file}}`

- Start a REPL (interactive shell):

`node`

- Evaluate JavaScript by passing it in the command:

`node -e "{{code}}"`

- Evaluate and print result, useful to see node's dependencies versions:

`node -p "{{process.versions}}"`

- Enable Node's inspector agent and pause execution until a debugger is connected. Prevent delayed (lazy) parsing of source code:

`node --no-lazy --inspect-brk {{path/to/file}}`
