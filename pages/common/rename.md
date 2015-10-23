# rename

> renames multiple files

- Change foo to bar in matching filenames

`rename {{'s/foo/bar/'}} {{*.txt}}`

- Convert to lower case

`rename -c {{*.txt}}`

- Replace whitespace with underscores

`rename --nows {{*.txt}}`
`rename 's/\s+/_/g' {{*.txt}}`

- No action, just show what renames would occur

`rename -n {{'s/foo/bar/'}} {{*.txt}}`
