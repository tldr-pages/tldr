# du

> Disk usage: estimate and summarize file and directory space usage.
> More information: <https://www.gnu.org/software/coreutils/du>.

- List the sizes of a directory and any subdirectories, in the given unit (B/KiB/MiB):

`du -{{b|k|m}} {{path/to/directory}}`

- List the sizes of a directory and any subdirectories, in human-readable form (i.e. auto-selecting the appropriate unit for each size):

`du -h {{path/to/directory}}`

- Show the size of a single directory, in human-readable units:

`du -sh {{path/to/directory}}`

- List the human-readable sizes of a directory and of all the files and directories within it:

`du -ah {{path/to/directory}}`

- List the human-readable sizes of a directory and any subdirectories, up to N levels deep:

`du -h --max-depth=N {{path/to/directory}}`

- List the human-readable size of all `.jpg` files in subdirectories of the current directory, and show a cumulative total at the end:

`du -ch {{*/*.jpg}}`
