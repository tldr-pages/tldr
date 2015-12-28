# find

> Find files under the given directory tree, recursively

- find files by extension

`find {{root_path}} -name {{'*.py'}}`

- find files modified since a certain time

`find {{root_path}} -name {{'*.py'}} -mtime {{-1d}}`

- find files using case insensitive name matching, of a certain size

`find {{root_path}} -size +500k -size -10MB -iname {{'*.TaR.gZ'}}`

- delete files by name, older than a certain number of days

`find {{root_path}} -name {{'*.py'}} -mtime {{-180d}} -delete`
