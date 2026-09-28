# alex

> Catch insensitive, inconsiderate writing.
> It helps you find gender favoring, polarizing, race related, religion inconsiderate, or other unequal phrasing in text.
> More information: <https://github.com/get-alex/alex>.

- Analyze text from `stdin`:

`echo {{His network looks good}} | alex --stdin`

- Analyze all files in the current directory:

`alex`

- Analyze a specific file:

`alex {{path/to/file.md}}`

- Analyze all Markdown files except a specified file:

`alex *.md !{{file.md}}`
