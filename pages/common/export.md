# export

> Command to mark shell variables in the current environment to be exported with any newly forked child processes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Set a new environment variable:

`export {{VARIABLE}}={{value}}`

- Remove an environment variable:

`export -n {{VARIABLE}}`

- Mark a shell function for export:

`export -f {{FUNCTION_NAME}}`

- Append something to the PATH variable:

`export PATH=$PATH:{{path/to/append}}`
