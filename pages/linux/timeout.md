# timeout

> Run a command with a time limit.

- Run sleep command (for 10 seconds) but kill it after 3 seconds:

`timeout 3s sleep 10`

- Run sleep command (for 10 seconds) but kill it when interruptted or after 5 seconds:

`timeout --signal INT 5s sleep 10`
