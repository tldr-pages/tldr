# watch

> Execute a command repeatedly, and monitor the output in full-screen mode

- monitor files in the current folder

`watch {{ls}}`

- monitor disk space and highlight the changes

`watch -d {{df}}`

- monitor "node" processes, refreshing every 3 seconds

`watch -n {{3}} "{{ps aux | grep node}}"`
