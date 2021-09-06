# vdir

> List directory contents.
> Drop-in replacement for `ls -l`.
> More information: <https://www.gnu.org/software/coreutils/vdir>.

- List files and directories in the current directory, one per line, with details:

`vdir`

- List with sizes displayed in human-readable units (KB, MB, GB):

`vdir -h`

- List including hidden files (starting with a dot):

`vdir -a`

- List files and directories sorting entries by size (largest first):

`vdir -S`

- List files and directories sorting entries by modification time (newest first):

`vdir -t`

- List grouping directories first:

`vdir --group-directories-first`

- Recursively list all files and directories in a specific directory:

`vdir --recursive {{path/to/directory}}`
