# du

> Estimate file space usage

- get a sum of the total size of a file/folder in human readable units

`du -sh {{file/directory}}`

- list file sizes of a directory and any subdirectories in KB

`du -k {{file/directory}}`

- get recursively, individual file/folder sizes in human readable form

`du -ah {{directory}}`

- list the KB sizes of directories for N levels below the specified directory

`du -k -depth=1 {{directory}}`
