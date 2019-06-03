# z

> Tracks the most used directories and enables quickly navigating to them using string or regex patterns.
> More information: <https://github.com/rupa/z>.

- Go to a directory that contains "foo" in the name:

`z {{foo}}`

- Go to a directory that contains "foo" and then "bar":

`z {{foo}} {{bar}}`

- Go to the highest-ranked directory matching "foo":

`z -r {{foo}}`

- Go to the most recently accessed directory matching "foo":

`z -t {{foo}}`

- List all directories in `z`'s database matching "foo":

`z -l {{foo}}`

- Remove the current directory from `z`'s database:

`z -x .`
