# rename.ul

> Renames multiple files.
> This is the util-linux version of `rename`. See `rename` for the perl version which is default on Debian.
> Warning: The renaming has no safeguards and will overwrite files without any questions.

- Rename files using simple substitutions (substitute 'foo' with 'bar' wherever found):

`rename {{foo}} {{bar}} {{*}}`

- Dry-run - display which renames would occur without performing them:

`rename -vn {{foo}} {{bar}} {{*}}`

- Do not overwrite existing files:

`rename -o {{foo}} {{bar}} {{*}}`

- Change file extensions:

`rename {{.ext}} {{.bak}} *.foo`

- Prepend all files with 'foo':

`rename '' 'foo' {{*}}`

- Rename 'foo1', ..., 'foo10', ..., 'foo100' to 'foo001', ..., 'foo010', ..., 'foo100':

`rename {{foo}} {{foo00}} {{foo?}} && rename {{foo}} {{foo0}} {{foo??}}`
