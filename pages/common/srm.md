# srm

> Securely remove files or directories
> Overwrites the existing data one or multiple. Drop in replacement for rm.

- Removes a file after overwriting (single pass, 7 pass, 35 pass)

`srm -s {{/path/to/file}}`
`srm -m {{/path/to/file}}`
`srm {{/path/to/file}}`

- Scurely remove recursively a directory and all it's subdirectories

`srm -r {{/path/to/folder}}`

- Prompt before every removal

`srm -i {{\*}}`
