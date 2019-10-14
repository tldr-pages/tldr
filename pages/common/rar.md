# rar

> An archive manager with compression ratio.

- Archive file/files:

`rar a {{archive_name.rar}} {{path/to/file1}} {{path/to/file2}} {{path/to/file3}}`

- Archive a directory:

`rar a {{archive_name.rar}} {{path/to/directory}}`

- Archive and split the file/files into parts of equal size (50M):

`rar a -v50M -R {{archive_name.rar}} {{path/to/file_or_directory}}`

- Archive with password protected:

`rar a -p{{password}} {{archive_name.rar}} {{path/to/file_or_directory}}`

- Archive, ecrypting file data and headers with password:

`rar a -hp{{password}} {{archive_name.rar}} {{path/to/file_or_directory}}`

- Archive with a specified compression level (0-5):

`rar a -m{{compression_level}} {{archive_name.rar}} {{path/to/file_or_directory}}`
