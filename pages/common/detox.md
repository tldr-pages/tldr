# detox

> Renames files to make them easier to work with.
> It removes spaces and other such annoyances like duplicate underline characters.
> More information: <https://github.com/dharple/detox>.

- Remove spaces and other undesirable characters from a file's name:

`detox {{path/to/file}}`

- Show how detox would rename all the files in a directory tree:

`detox --dry-run -r {{path/to/directory}}`

- Remove spaces and other undesirable characters from all files in a directory tree:

`detox -r {{path/to/directory}}`
