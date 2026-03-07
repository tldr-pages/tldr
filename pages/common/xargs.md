# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines, and end-of-file.
> See also: `parallel`.
> More information: <https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs>.

- Run a command using the input data as arguments:

`{{arguments_source}} | xargs {{command}}`

- Run multiple chained commands on the input data:

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- Execute a new command with each argument:

`{{arguments_source}} | xargs {{[-n|--max-args]}} 1 {{command}}`

- Raise the parallel process limit to 10 (default is 1). If the number is 0, xargs will run as many processes as possible at a time:

`{{arguments_source}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{command}}`

- Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- Prompt user for confirmation before executing command (confirm with `y` or `Y`):

`{{arguments_source}} | xargs {{[-p|--interactive]}} {{command}}`

- Read a file for arguments to be given to a command:

`xargs {{[-a|--arg-file]}} {{path/to/file}} {{command}}`

- Allow the command to access the terminal for interactive input:

`{{arguments_source}} | xargs {{[-o|--open-tty]}} {{command}}`
