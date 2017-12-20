# export

> Command to mark shell variables in the current environment to be exported with any newly forked child processes.

- Set a new environment variable:

`export {{VARIABLE}}={{value}}`

- Remove an environment variable:

`export -n {{VARIABLE}}`

- Append something to the PATH variable:

`export PATH=$PATH:{{path/to/append}}`
