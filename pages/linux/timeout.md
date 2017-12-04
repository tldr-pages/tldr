# timeout

> Run a command with a time limit.

- Run `sleep 10` and kill it, if it's running after 3 seconds:

`timeout {{3s}} {{sleep 10}}`

- Specify the signal to be sent to the command after the time limit expires. (By default, TERM is sent):

`timeout --signal {{INT}} {{5s}} {{sleep 10}}`
