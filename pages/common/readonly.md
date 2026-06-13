# readonly

> Set read-only shell variables.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-readonly>.

- Set a read-only variable:

`readonly {{variable_name}}={{value}}`

- Mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint the names and values of all read-only variables to `stdout`:

`readonly -p`
