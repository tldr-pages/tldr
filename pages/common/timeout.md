# timeout

> Run a command with a time limit.
> More information: <https://www.gnu.org/software/coreutils/timeout>.

- Run `sleep 10` and terminate it after 3 seconds:

`timeout 3s sleep 10`

- Send a signal to the command after the time limit expires (SIGTERM by default):

`timeout --signal {{INT}} {{5s}} {{sleep 10}}`
