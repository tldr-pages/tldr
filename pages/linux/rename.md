# rename

> Rename multiple files.
> Note: this page refers to the command from the `util-linux` package.
> For the Perl version, see `file-rename` or `perl-rename`.
> Warning: This command has no safeguards and will overwrite files without prompting.
> More information: <https://manned.org/rename>.

- Rename files using simple substitutions (substitute 'foo' with 'bar' wherever found):

`rename {{foo}} {{bar}} {{*}}`

- Dry-run - display which renames would occur without performing them:

`rename -vn {{foo}} {{bar}} {{*}}`

- Do not overwrite existing files:

`rename -o {{foo}} {{bar}} {{*}}`

- Change file extensions:

`rename {{.ext}} {{.bak}} {{*.ext}}`

- Prepend "foo" to all filenames in the current directory:

`rename {{''}} {{'foo'}} {{*}}`

- Rename a group of increasingly numbered files zero-padding the numbers up to 3 digits:

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
