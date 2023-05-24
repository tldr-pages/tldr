# mv

> Move or rename files and directories.
> More information: <https://www.gnu.org/software/coreutils/mv>.

- Rename a file or directory when the target is not an existing directory:

`mv {{path/to/source}} {{path/to/target}}`

- Move a file or directory into an existing directory:

`mv {{path/to/source}} {{path/to/existing_directory}}`

- Move multiple files into an existing directory, keeping the filenames unchanged:

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- Do not prompt for confirmation before overwriting existing files:

`mv -f {{path/to/source}} {{path/to/target}}`

- Prompt for confirmation before overwriting existing files, regardless of file permissions:

`mv -i {{path/to/source}} {{path/to/target}}`

- Do not overwrite existing files at the target:

`mv -n {{path/to/source}} {{path/to/target}}`

- Move files in verbose mode, showing files after they are moved:

`mv -v {{path/to/source}} {{path/to/target}}`
