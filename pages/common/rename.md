# rename

> Renames multiple files.

- Rename files using a Perl Common Regular Expression (substitute 'foo' with 'bar' wherever found):

`rename {{'s/foo/bar/'}} {{\*}}`

- Dry-run, display which renames would occur without performing them:

`rename -n {{'s/foo/bar/'}} {{\*}}`

- Convert filenames to lower case:

`rename 'y/A-Z/a-z/' {{\*}}`

- Replace whitespace with underscores:

`rename 's/\s+/_/g' {{\*}}`
