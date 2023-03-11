# z

> Maintains a jump-list of your most used (by 'frecency') directories, and enables quickly navigating to them using string patterns or regular expressions.
> More information: <https://github.com/rupa/z>.

- Go to the most frecent directory that contains "foo" in the name:

`z {{foo}}`

- Go to the most frecent directory containing "foo" and "bar", in order:

`z {{foo}} {{bar}}`

- Go to the highest ranked (most used) directory contaning "foo":

`z -r {{foo}}`

- Go to the most recently accessed directory contaning "foo":

`z -t {{foo}}`

- List all directories in the jump-list containing "foo":

`z -l {{foo}}`

- Remove the current directory from the jump-list:

`z -x .`

- Restrict matches to subdirectories of the current directory:

`z -c {{foo}}`

- Show a brief help message

`z -h`
