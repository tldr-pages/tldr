# rar

> The RAR archiver. Supports multi-volume archives that can be optionally self-extracting.

- Archive file/files:

`rar a {{path/to/archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Archive a directory:

`rar a {{path/to/archive_name.rar}} {{path/to/directory}}`

- Split the archive into parts of equal size (50M):

`rar a -v50M -R {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Archive with password protected:

`rar a -p{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Archive, ecrypting file data and headers with password:

`rar a -hp{{password}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`

- Archive with a specified compression level (0-5):

`rar a -m{{compression_level}} {{path/to/archive_name.rar}} {{path/to/file_or_directory}}`
