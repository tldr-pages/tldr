# export

> Export shell variables to child processes.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- Set an environment variable:

`export {{VARIABLE}}={{value}}`

- Unset an environment variable:

`export -n {{VARIABLE}}`

- Export a [f]unction to child processes:

`export -f {{FUNCTION_NAME}}`

- Append a pathname to the environment variable `$PATH`:

`export PATH=$PATH:{{path/to/append}}`

- [p]rint a list of active exported variables in shell command form:

`export -p`
