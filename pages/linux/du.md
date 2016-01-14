# du

> Estimate file space usage.

- Get a sum of the total size of a file/folder in human readable units:

`du -sh {{file/directory}}`

- List file sizes of a directory and any subdirectories in KB/MB:

`du -k {{file/directory}}`
`du -m {{file/directory}}`

- Get recursively, individual file/folder sizes in human readable form:

`du -ah {{directory}}`

- List the KB sizes of directories for N levels below the specified directory:

`du --max-depth=N`
