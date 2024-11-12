# difft

> Compare files or directories based on the syntax of the programming language.
> See also: `delta`, `diff`.
> More information: <https://difftastic.wilfred.me.uk/introduction.html>.

- Compare two files or directories:

`difft {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Only report the presence of differences between the files:

`difft --check-only {{path/to/file1}} {{path/to/file2}}`

- Specify the display mode (default is `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{path/to/file1}} {{path/to/file2}}`

- Ignore comments when comparing:

`difft --ignore-comments {{path/to/file1}} {{path/to/file2}}`

- Enable/Disable syntax highlighting of source code (default is `on`):

`difft --syntax-highlight {{on|off}} {{path/to/file1}} {{path/to/file2}}`

- Do not output anything at all if there are no differences between files:

`difft --skip-unchanged {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Print all programming languages supported by the tool, along with their extensions:

`difft --list-languages`
