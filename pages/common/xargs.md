# xargs

> Execute a command with piped arguments coming from another command, a file, etc.
> The input is treated as a single block of text and split into separate arguments on spaces, tabs, newlines and end-of-file.

- Main usage pattern:

`{{arguments_source}} | xargs {{command}}`

- Delete all files with a `.backup` extension. Use the `--delimiter`/`-d` flag to split based on a specific whitespace character (useful if there's spaces in the filenames):

`find . -name {{'*.backup'}} | xargs --delimiter '\n' rm -v`

- Execute the command once for each input line, replacing any occurrences of the placeholder (here marked as `_`) with the input line:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`
