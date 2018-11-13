# rm

> Remove files or directories.

- Remove files from arbitrary locations:

`rm {{path/to/file}} {{path/to/another/file}}`

- Recursively remove a directory and all its subdirectories:

`rm -r {{path/to/folder}}`

- Forcibly remove a directory, without prompting for confirmation or showing error messages:

`rm -rf {{path/to/folder}}`

- Interactively remove multiple files, with a prompt before every removal:

`rm -i {{file(s)}}`

- Remove files in verbose mode, printing a message for each removed file:

`rm -v {{path/to/folder/*}}`
