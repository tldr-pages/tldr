# du

> Disk usage: estimate and summarize file and folder space usage.

- Get a sum of the total size of a file/folder, in human readable units:

`du -sh {{file_or_folder}}`

- List file sizes of a folder and any subfolders, in KB:

`du -k {{file_or_folder}}`

- List file sizes of a folder and any subfolders, in MB:

`du -m {{file_or_folder}}`

- Get individual file/folder sizes, recursively, in human readable form:

`du -ah {{folder}}`

- List the KB sizes of folders for N levels below the specified folder:

`du --max-depth=N`

- Get the total size of all .jpg files in subfolders of the current folder:

`du -ch */*.jpg`
