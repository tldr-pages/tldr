# atool

> A script for managing file archives of various types.
> `atool` uses external archiver programs but provides a consistent command-line interface for listing, extracting, creating, and managing archives.
> More information: <https://savannah.nongnu.org/projects/atool/>.

- Extract an archive (safely creates a subdirectory if needed):

`atool -x {{archive.tar.gz}}`

- Extract an archive to a specific directory:

`atool -X {{path/to/output_directory}} {{archive.rar}}`

- List files in an archive:

`atool -l {{archive.zip}}`

- Display a specific file's content from an archive to standard output (like `cat`):

`atool -c {{archive.tar}} {{path/to/file_in_archive.txt}}`

- Create a new archive from specified files and/or directories:

`atool -a {{new_archive.zip}} {{file1.txt}} {{directory_name}}`

- List files in an archive and send the output through a pager:

`atool -l -p {{large_archive.tar.bz2}}`

- Extract multiple archives at once (each to its own subdirectory if needed):

`atool -x -e {{archive1.zip}} {{archive2.tar.gz}} {{*.rar}}`

- Repack an archive from one format to another (e.g., .tar.gz to .tar.7z):

`atool -r {{old_archive.tar.gz}} {{new_archive.tar.7z}}`
