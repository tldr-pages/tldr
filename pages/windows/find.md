# find

> Find a specified string in one or more files.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/find>.

- Find lines that contain a specified string:

`find "{{string}}" {{path/to/file_or_directory}}`

- Display lines that do not contain the specified string:

`find "{{string}}" {{path/to/file_or_directory}} /v`

- Display the count of lines that contain the specified string:

`find "{{string}}" {{path/to/file_or_directory}} /c`

- Display line numbers with the list of lines:

`find "{{string}}" {{path/to/file_or_directory}} /n`
