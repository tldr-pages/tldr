# watch

> Execute a command repeatedly, and monitor the output in full-screen mode.

- Monitor files in the current directory:

`watch {{ls}}`

- Monitor disk space and highlight the changes:

`watch -d {{df}}`

- Monitor "node" processes, refreshing every 3 seconds:

`watch -n {{3}} "{{ps aux | grep node}}"`
