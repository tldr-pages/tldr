# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate pieces on spaces, tabs, newlines and end-of-file.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Run a command using the input data as arguments:

`{{arguments_source}} | xargs {{command}}`

- Run multiple chained commands on the input data:

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- Delete all files with a `.backup` extension (`-print0` uses a null character to split file names, and `-0` uses it as delimiter):

`find . -name {{'*.backup'}} -print0 | xargs -0 rm -v`

- Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- Parallel runs of up to `max-procs` processes at a time; the default is 1. If `max-procs` is 0, xargs will run as many processes as possible at a time:

`{{arguments_source}} | xargs -P {{max-procs}} {{command}}`
