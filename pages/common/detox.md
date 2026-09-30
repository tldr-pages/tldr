# detox

> Renames files to make them easier to work with.
> It removes spaces and other such annoyances like duplicate underline characters.
> More information: <https://manned.org/detox>.

- Remove spaces and other undesirable characters from a file's name:

`detox {{path/to/file}}`

- Simulate renaming all the files in a directory tree, showing how they would be renamed:

`detox {{[-n|--dry-run]}} -r {{path/to/directory}}`

- Remove spaces and other undesirable characters from all files in a directory tree:

`detox -r {{path/to/directory}}`
