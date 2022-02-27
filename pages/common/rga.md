# rga

> Ripgrep wrapper with rich file type searching capabilities.
> More information: <https://github.com/phiresky/ripgrep-all>.

- Recursively search the current directory for a regular expression:

`rga {{regular_expression}}`

- List available adapters:

`rga --rga-list-adapters`

- Change which adapters to use (e.g. ffmpeg, pandoc, poppler etc.):

`rga --rga-adapters={{adapter1,adapter2}} {{regular_expression}}`

- Use more accurate but slower matching by mime type:

`rga --rga-accurate {{regular_expression}}`

- Show detailed help:

`rga --help`
