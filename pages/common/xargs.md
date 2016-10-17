# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate arguments on spaces, tabs, newlines and end-of-file.

- Main usage pattern:

`{{arguments_source}} | xargs {{command}}`

- Delete all files with a `.backup` extension:

`{{find . -name '*.backup'}} | xargs {{rm -v}}`

- Convert newlines in the input into NUL (`\0`) characters, and split on those only (useful if the input to xargs contains spaces):

`{{arguments_source}} | tr '\n' '\0' | xargs -0 {{command}}`

- Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`
