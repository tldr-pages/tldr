# bat

> Print and concatenate files.
> A `cat` clone with syntax highlighting and Git integration.

- Print the contents of a file to the standard output:

`bat {{file}}`

- Concatenate several files into the target file:

`bat {{file1}} {{file2}} > {{target_file}}`

- Append several files into the target file:

`bat {{file1}} {{file2}} >> {{target_file}}`

- Number all output lines:

`bat -n {{file}}`

- Syntax highlight a json file:

`bat --language json {{file.json}}`

- Display all supported languages:

`bat --list-languages`
