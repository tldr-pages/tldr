# rename

> Renames multiple files.

- Rename files using a Perl Common Regular Expression (substitute 'foo' with 'bar' wherever found):

`rename {{'s/foo/bar/'}} {{\*}}`

- Dry-run - display which renames would occur without performing them:

`rename -n {{'s/foo/bar/'}} {{\*}}`

- Force renaming even if the operation would overwrite existing files:

`rename -f {{'s/foo/bar/'}} {{\*}}`

- Convert filenames to lower case (use `-f` in case-insensitive filesystems to prevent "already exists" errors):

`rename 'y/A-Z/a-z/' {{\*}}`

- Replace whitespace with underscores:

`rename 's/\s+/_/g' {{\*}}`
