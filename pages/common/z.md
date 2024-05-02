# z

> Tracks the most used (by frequency) directories and enables quickly navigating to them using string patterns or regular expressions.
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

- Restrict matches to subdirectories of the current directory:

`z -c {{foo}}`

- Interactive selection of the directories (Needs `fzf` v0.33.0 and above):

`zi`

- Enter partial name or if there are more than one directories with similar names, it will allow you to interactively select the one:

`zi {{foo}}`
