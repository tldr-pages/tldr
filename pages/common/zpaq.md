# zpaq

> Incremental Journaling Backup Utility and Archiver.
> More information: <https://mattmahoney.net/dc/zpaq.html>.

- [a]dd a file or directory to a new or existing archive:

`zpaq a {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- Create or add to encrypted archive:

`zpaq a -k{{password}} {{path/to/archive.zpaq}} {{path/to/file_or_directory}}`

- E[x]tract the most recent recent versions of files:

`zpaq x {{path/to/archive.zpaq}}`

- [l]ist or compare external files to archive by dates:

`zpaq l {{path/to/archive.zpaq}}`

- Set the level of compression (higher means more compression but slower):

`zpaq a {{path/to/archive.zpaq}} -m{{1|2|3|4|5}} {{path/to/file_or_directory}}`

- E[x]tract to directory as of the date or version number:

`zpaq x {{path/to/archive.zpaq}} {{path/to/extract}} -to {{path/to/output}} -until {{YYYY-MM-DD}}`
