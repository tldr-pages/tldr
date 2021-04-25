# find

> Find files or directories under the given directory tree, recursively.
> More information: <https://manned.org/find>.

- Find files by extension:

`find {{root_path}} -name '{{*.ext}}'`

- Find files by matching multiple patterns:

`find {{root_path}} -name '{{*pattern_1*}}' -or -name '{{*pattern_2*}}'`

- Find directories matching a given name, in case-insensitive mode:

`find {{root_path}} -type d -iname '{{*lib*}}'`

- Find files matching a path pattern:

`find {{root_path}} -path '{{**/lib/**/*.ext}}'`

- Find files matching a given pattern, excluding specific paths:

`find {{root_path}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Find files matching a given size range:

`find {{root_path}} -size {{+500k}} -size {{-10M}}`

- Run a command for each file (use `{}` within the command to access the filename):

`find {{root_path}} -name '{{*.ext}}' -exec {{wc -l {} }}\;`

- Find files modified in the last 7 days, and delete them:

`find {{root_path}} -mtime {{-7}} -delete`
