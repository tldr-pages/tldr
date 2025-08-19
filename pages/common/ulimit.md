# ulimit

> Get and set resource limits for user processes.
> It is a shell builtin hence not shell-agnostic.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-ulimit>.

- Get the properties of all the user limits:

`ulimit -a`

- Get hard limit for the number of simultaneously opened files:

`ulimit -H -n`

- Get soft limit for the number of simultaneously opened files:

`ulimit -S -n`

- Set max per-user process limit:

`ulimit -u {{30}}`

- Display help (Bash only):

`help ulimit`
