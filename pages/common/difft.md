# difft

> Compare files or directories based on the syntax of the programming language.
> More information: <https://difftastic.wilfred.me.uk/introduction.html>.

- Check files or directories for changes:

`difft {{path/to/original_file_or_directory}} {{path/to/new_file_or_directory}}`

- Only report if there are changes between the source code files:

`difft --check-only {{path/to/original_file}} {{path/to/new_file}}`

- Show changes in different display modes (default mode is `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{path/to/original_file}} {{path/to/new_file}}`

- Ignore comments when diffing:

`difft --ignore-comments {{path/to/original_file}} {{path/to/new_file}}`

- Turn on syntax highlighting of source code on or off (default is `on`):

`difft --syntax-highlight {{on|off}} {{path/to/original_file}} {{path/to/new_file}}`

- Do not output anything at all if there are no changes between files:

`difft --skip-unchanged {{path/to/original_file}} {{path/to/new_file}}`

- Print all the languages supported by difftastic, along with their extensions:

`difft --list-languages`
