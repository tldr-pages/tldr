# rbash

> Restricted Bash shell, equivalent to `bash --restricted`.
> Does not permit changing the working directory, redirecting command output, or modifying environment variables, among other things.
> See also `histexpand` for history expansion.
> More information: <https://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell>.

- Start an interactive shell session:

`rbash`

- Execute a command and then exit:

`rbash -c "{{command}}"`

- Execute a script:

`rbash {{path/to/script.sh}}`

- Execute a script, printing each command before executing it:

`rbash -x {{path/to/script.sh}}`

- Execute commands from a script, stopping at the first error:

`rbash -e {{path/to/script.sh}}`

- Read and execute commands from stdin:

`rbash -s`
