# mv

> Move or rename files and directories.
> More information: <https://www.gnu.org/software/coreutils/mv>.

- Rename a file or directory when the target is not an existing directory:

`mv {{path/to/source}} {{path/to/target}}`

- Move a file or directory into an existing directory:

`mv {{path/to/source}} {{path/to/existing_directory}}`

- Move multiple files into an existing directory, keeping the filenames unchanged:

`mv {{path/to/source1 path/to/source2 ...}} {{path/to/existing_directory}}`

- Do not prompt ([f]) for confirmation before overwriting existing files:

`mv --force {{path/to/source}} {{path/to/target}}`

- Prompt for confirmation [i]nteractively before overwriting existing files, regardless of file permissions:

`mv --interactive {{path/to/source}} {{path/to/target}}`

- Do not overwrite ([n]) existing files at the target:

`mv --no-clobber {{path/to/source}} {{path/to/target}}`

- Move files in [v]erbose mode, showing files after they are moved:

`mv --verbose {{path/to/source}} {{path/to/target}}`

- Specify [t]arget directory so that you can use external tools to gather movable files:

`{{find /var/log -type f -name '*.log' -print0}} | {{xargs -0}} mv --target-directory {{path/to/target_directory}}`
