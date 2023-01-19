# mv

> Move or rename files and directories.
> More information: <https://www.gnu.org/software/coreutils/mv>.

- Rename a file or directory when the target is not an existing directory:

`mv {{source}} {{target}}`

- Move a file or directory into an existing directory:

`mv {{source}} {{existing_directory}}`

- Move multiple files into an existing directory, keeping the filenames unchanged:

`mv {{source1}} {{source2}} {{source3}} {{existing_directory}}`

- Do not prompt for confirmation before overwriting existing files:

`mv -f {{source}} {{target}}`

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -i {{source}} {{target}}`

- Do not overwrite existing files at the target:

`mv -n {{source}} {{target}}`

- Move files in verbose mode, showing files after they are moved:

`mv -v {{source}} {{target}}`
