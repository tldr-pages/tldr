# difftastic

> A structural diff tool that compares files based on their syntax.
> More information: <https://difftastic.wilfred.me.uk>.

- Compare two files:

`difft {{path/to/file1}} {{path/to/file2}}`

- Compare files using git diff with difftastic:

`git diff --ext-diff`

- Display a side-by-side diff:

`difft --display {{side-by-side}} {{path/to/file1}} {{path/to/file2}}`

- Ignore comments when comparing:

`difft --ignore-comments {{path/to/file1}} {{path/to/file2}}`

- Compare two directories recursively:

`difft --recursive {{path/to/directory1}} {{path/to/directory2}}`

- Set a specific language for syntax parsing:

`difft --language {{rust}} {{path/to/file1}} {{path/to/file2}}`

- Show only the changed hunks without context:

`difft --context {{0}} {{path/to/file1}} {{path/to/file2}}`

- Display the list of supported languages:

`difft --list-languages`
