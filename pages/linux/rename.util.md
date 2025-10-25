# rename

> Rename multiple files.
> WARNING: This command will overwrite files without prompting unless the dry-run option is used.
> Note: This page refers to the command from the `util-linux` package.
> More information: <https://manned.org/rename>.

- Rename files using simple substitutions (substitute 'foo' with 'bar' wherever found):

`rename {{foo}} {{bar}} {{*}}`

- Dry-run - display which renames would occur without performing them:

`rename {{[-vn|--verbose --no-act]}} {{foo}} {{bar}} {{*}}`

- Do not overwrite existing files:

`rename {{[-o|--no-overwrite]}} {{foo}} {{bar}} {{*}}`

- Change file extensions:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Prepend "foo" to all filenames in the current directory:

`rename '' '{{foo}}' {{*}}`

- Rename a group of increasingly numbered files zero-padding the numbers up to 3 digits:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
