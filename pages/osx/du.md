# du

> Estimate file space usage.

- Get a sum of the total size of a file/folder in human readable units:

`du -sh {{path/to/file_or_folder}}`

- List file sizes of a directory and any subdirectories in KB:

`du -k {{path/to/file_or_folder}}`

- Get recursively, individual file/folder sizes in human readable form:

`du -ah {{path/to/folder}}`

- List the human-readable sizes of directories for 2 levels of depth below the specified directory:

`du -h -d 2 {{path/to/folder}}`
