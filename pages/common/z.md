# z

> Tracks your most used directories and enable quick jumping using regexes from the command line.

- Go to a directory that contains a regex:

`z {{regexp}}`

- Go to a directory that contains regex1 and then regex2:

`z {{regex1}} {{regex2}}`

- Go to the highest ranked directory matching a regex:

`z -r {{regex}}`

- Go to the most recently accessed directory matching a regex:

`z -t {{regex}}`

- List all directories matching a {{regex}} (from z datafile):

`z -l regex`

- Remove the current directory from the datafile:

`z -x .`
