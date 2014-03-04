# rename

> renames multiple files

- Change foo to bar in matching files

`rename {{'s/foo/bar/'}} {{*.txt}}`

- Convert to lower case

`rename -c {{*.txt}}`

- Replace whitespace with underscores

`rename --nows {{*.txt}}`
