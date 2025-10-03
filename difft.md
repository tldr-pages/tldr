# difft

> Compare files or directories based on the syntax of the programming language.
> See also: `delta`, `diff`.
> More information: <https://difftastic.wilfred.me.uk/introduction.html>.

- Compare two files or directories:

`difft {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- Use difftastic from Git:

`git diff --ext-diff`

- Only report whether differences exist:

`difft --check-only {{path/to/file1}} {{path/to/file2}}`

- Specify the display mode (default is `side-by-side`):

`difft --display {{side-by-side|side-by-side-show-both|inline|json}} {{path/to/file1}} {{path/to/file2}}`

- Show only the changed hunks without any surrounding context:
  
`difft --context 0 {{path/to/file1}} {{path/to/file2}}`

- Ignore comments when comparing:

`difft --ignore-comments {{path/to/file1}} {{path/to/file2}}`

- Enable/disable syntax highlighting (default is `on`):

`difft --syntax-highlight {{on|off}} {{path/to/file1}} {{path/to/file2}}`

- Do not output anything if there are no differences:

`difft --skip-unchanged {{path/to/file_or_directory1}} {{path/to/file_or_directory2}}`

- List supported languages and extensions:

`difft --list-languages`
