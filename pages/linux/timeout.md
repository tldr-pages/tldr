# timeout

> Run a command with a time limit.

- Run `sleep 10` with a time limit of 3 seconds:

`timeout {{3s}} {{sleep 10}}`

- Run `sleep 10` with a time limit of 5 seconds or kill it when interruptted:

`timeout {{--signal INT}} {{5s}} {{sleep 10}}`
