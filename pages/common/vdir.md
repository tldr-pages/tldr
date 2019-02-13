# vdir

> List directory contents.
> Drop-in replacement for `ls -l`.

- List files in the current directory, one per line, with details:

`vdir`

- List files with size displayed using human readable units (KB, MB, GB):

`vdir -h`

- List all files, including hidden files (starting with a dot):

`vdir -a`

- List files sorting them by size (largest first):

`vdir -S`

- List files sorting them by modification time (newest first):

`vdir -t`

- List files grouping directories first:

`vdir --group-directories-first`

- Recursively list files in a specific directory:

`vdir --recursive {{path/to/directory}}`
