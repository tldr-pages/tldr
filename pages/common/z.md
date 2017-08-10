# z

> Tracks your most used directories and enable quick jumping using regexes from the command line.

- Go to a directory that contains foo:

`z {{foo}}`

- Go to a directory that contains foo and then bar:

`z {{foo}} {{bar}}`

- Go to the highest ranked directory matching foo:

`z -r {{foo}}`

- Go to the most recently accessed directory matching foo:

`z -t {{foo}}`

- List all directories matching foo (from z database):

`z -l {{foo}}`

- Remove the current directory from the database:

`z -x .`
