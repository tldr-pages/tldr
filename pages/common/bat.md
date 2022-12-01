# bat

> Print and concatenate files.
> A `cat` clone with syntax highlighting and Git integration.
> More information: <https://github.com/sharkdp/bat>.

- Print the contents of a file to the standard output:

`bat {{path/to/file}}`

- Concatenate several files into the target file:

`bat {{path/to/file1}} {{path/to/file2}} > {{target_file}}`

- Append several files into the target file:

`bat {{path/to/file1}} {{path/to/file2}} >> {{target_file}}`

- Number all output lines:

`bat -n {{path/to/file}}`

- Syntax highlight a JSON file:

`bat --language json {{path/to/file.json}}`

- Display all supported languages:

`bat --list-languages`
