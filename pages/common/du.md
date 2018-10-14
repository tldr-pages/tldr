# du

> Disk usage: estimate and summarize file and folder space usage.

- List the sizes of a folder and any subfolders, in the given unit (B/KB/MB):

`du -{{b|k|m}} {{path/to/folder}}`

- List the sizes of a folder and any subfolders, in human-readable form (i.e. auto-selecting the appropriate unit for each size):

`du -h {{path/to/folder}}`

- Show the size of a single folder, in human readable units:

`du -sh {{path/to/folder}}`

- List the human-readable sizes of a folder and of all the files and folders within it:

`du -ah {{path/to/folder}}`

- List the human-readable sizes of a folder and any subfolders, up to N levels deep:

`du -h --max-depth=N {{path/to/folder}}`

- List the human-readable size of all .jpg files in subfolders of the current folder, and show a cumulative total at the end:

`du -ch */*.jpg`
