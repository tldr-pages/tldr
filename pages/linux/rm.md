# rm

> Removes files or directories.
> More information: <https://www.gnu.org/software/coreutils/rm>.

- Remove files from arbitrary locations:

`rm {{path/to/file}} {{path/to/another/file}}`

- Recursively remove a directory and all its subdirectories:

`rm --recursive {{path/to/directory}}`

- Forcibly remove a directory, without prompting for confirmation or showing error messages:

`rm --recursive --force {{path/to/directory}}`

- Interactively remove multiple files, with a prompt before every removal:

`rm --interactive {{file(s)}}`

- Remove files in verbose mode, printing a message for each removed file:

`rm --verbose {{path/to/directory/*}}`
