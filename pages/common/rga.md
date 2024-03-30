# rga

> Ripgrep wrapper with rich file type searching capabilities.
> More information: <https://github.com/phiresky/ripgrep-all>.

- Search recursively for a pattern in all files in the current directory:

`rga {{regular_expression}}`

- List available adapters:

`rga --rga-list-adapters`

- Change which adapters to use (e.g. ffmpeg, pandoc, poppler etc.):

`rga --rga-adapters={{adapter1,adapter2}} {{regular_expression}}`

- Search for a pattern using the mime type instead of the file extension (slower):

`rga --rga-accurate {{regular_expression}}`

- Display help:

`rga --help`
