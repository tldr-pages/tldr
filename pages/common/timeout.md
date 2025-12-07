# timeout

> Run a command with a time limit.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- Run `sleep 10` and terminate it after 3 seconds:

`timeout 3s sleep 10`

- Send a signal to the command after the time limit expires (`TERM` by default, `kill -l` to list all signals):

`timeout {{[-s|--signal]}} {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- Send verbose output to `stderr` showing signal sent upon timeout:

`timeout {{[-v|--verbose]}} {{0.5s|1m|1h|1d|...}} {{command}}`

- Preserve the exit status of the command regardless of timing out:

`timeout {{[-p|--preserve-status]}} {{1s|1m|1h|1d|...}} {{command}}`

- Send a forceful `KILL` signal after certain duration if the command ignores initial signal upon timeout:

`timeout {{[-k|--kill-after]}} {{5m}} {{30s}} {{command}}`

- Print timeout signals to `stderr`:

`timeout {{[-v|--verbose]}}`
