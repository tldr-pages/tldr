# find

> Find files under the current directory tree, recursively

- find files by extension

`find {{root_path}} -name {{'*.py'}}`

- run a command for each file

`find {{root_path}} -name {{'*.py'}} -exec {{wc -l {}}} \;`

- find files modified since a certain time

`find {{root_path}} -name {{'*.py'}} -mtime {{-1d}}`
