# while

> Simple shell loop.
> More information: <https://manned.org/while>.

- Read stdin and perform an action on every line:

`while read line; do echo "$line"; done`

- Execute a command forever once every second:

`while :; do {{command}}; sleep 1; done`
