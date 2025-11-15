# zpaq

> Incremental journaling backup utility and archiver.
> More information: <https://mattmahoney.net/dc/zpaqdoc.html>.

- Add a file or directory to a new or existing archive:

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- Create or add to an encrypted archive:

`zpaq {{[a|add]}} -k{{password}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- Extract the most recent versions of files:

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}}`

- List the archive contents:

`zpaq {{[l|list]}} {{path/to/archive.zpaq}}`

- Set the level of compression (higher means more compression but slower):

`zpaq {{[a|add]}} {{path/to/archive.zpaq}} -m{{1|2|3|4|5}} {{path/to/file_or_directory}}`

- Extract the specified files from the archive that are not newer than the specified date:

`zpaq {{[x|extract]}} {{path/to/archive.zpaq}} {{path/in/archive/to/extract}} -to {{path/to/output}} -until {{YYYY-MM-DD}}`
