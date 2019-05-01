# srm

> Securely remove files or directories.
> Overwrites the existing data one or multiple times. Drop in replacement for rm.

- Remove a file after a single-pass overwriting with random data:

`srm -s {{/path/to/file}}`

- Remove a file after seven passes of overwriting with random data:

`srm -m {{/path/to/file}}`

- Recursively remove a directory and its contents overwriting each file with a single-pass of random data:

`srm -r -s {{/path/to/directory}}`

- Prompt before every removal:

`srm -i {{\*}}`
