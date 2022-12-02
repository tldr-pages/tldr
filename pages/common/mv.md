# mv

> Move or rename files and directories.
> More information: <https://www.gnu.org/software/coreutils/mv>.

- Move a file to an arbitrary location:

`mv {{path/to/source}} {{target}}`

- Move files into another directory, keeping the filenames:

`mv {{source1 source2 ...}} {{path/to/directory}}`

- Do not prompt for confirmation before overwriting existing files:

`mv -f {{path/to/source}} {{target}}`

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -i {{path/to/source}} {{target}}`

- Do not overwrite existing files at the target:

`mv -n {{path/to/source}} {{target}}`

- Move files in verbose mode, showing files after they are moved:

`mv -v {{path/to/source}} {{target}}`
