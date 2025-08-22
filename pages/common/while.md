# while

> Simple shell loop that repeats while the return value remains zero.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-while>.

- Read `stdin` and perform an action on every line:

`while read line; do {{echo "$line"}}; done`

- Execute a command forever once every second:

`while :; do {{command}}; sleep 1; done`

- Execute a command until it fails:

`while {{command}}; do :; done`
