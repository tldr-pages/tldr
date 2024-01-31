# bat

> Print and concatenate files.
> A `cat` clone with syntax highlighting and Git integration.
> More information: <https://github.com/sharkdp/bat>.

- Print the contents of one or more files to `stdout`:

`bat {{path/to/file1 path/to/file2 ...}}`

- Concatenate several files into the target file:

`bat {{path/to/file1 path/to/file2 ...}} > {{path/to/target_file}}`

- Append several files into the target file:

`bat {{path/to/file1 path/to/file2 ...}} >> {{path/to/target_file}}`

- Number all output lines:

`bat --number {{path/to/file}}`

- Syntax highlight a JSON file:

`bat --language json {{path/to/file.json}}`

- Display all supported languages:

`bat --list-languages`
