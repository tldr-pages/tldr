# find

> Find files under the given directory tree, recursively.

- Find files by extension:

`find {{root_path}} -name '{{*.ext}}'`

- Find files matching path pattern:

`find {{root_path}} -path '{{**/lib/**/*.ext}}'`

- Run a command for each file, use {} within the command to access the filename:

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Find files modified since a certain time:

`find {{root_path}} -name '{{}}' -mtime {{-1}}`

- Find files using case insensitive name matching, of a certain size:

`find {{root_path}} -size +500k -size -10MB -iname '{{*.TaR.gZ}}'`

- Delete files by name, older than a certain number of days:

`find {{root_path}} -name '{{*.ext}}' -mtime {{-180}} -delete`

- Find empty files or directories:

`find {{root_path}} -empty`

- Find files matching more than one search criteria:

`find {{root_path}} -name '{{*.py}}' -or -name '{{*.r}}'`
