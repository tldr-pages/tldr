# rename

> Rename multiple files.
> WARNING: This command will overwrite files without prompting unless the `--no-act` option is used.
> Note: This page refers to the command from the `util-linux` package.
> More information: <https://manned.org/rename>.

- Rename files using simple substitutions (substitute a string with a replacement wherever found):

`rename {{string}} {{replacement}} {{*}}`

- Simulate running the program without doing anything:

`rename {{[-vn|--verbose --no-act]}} {{string}} {{replacement}} {{*}}`

- Do not overwrite existing files:

`rename {{[-o|--no-overwrite]}} {{string}} {{replacement}} {{*}}`

- Change file extensions:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Prepend a prefix to all filenames in the current directory:

`rename '' '{{prefix}}' {{*}}`

- Rename a group of increasingly numbered files zero-padding the numbers up to 3 digits:

`rename {{prefix}} {{prefix00}} {{prefix?}} && rename {{prefix}} {{prefix0}} {{prefix??}}`
