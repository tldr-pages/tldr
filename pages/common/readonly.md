# readonly

> Set read-only shell variables.
> More information: <https://manned.org/readonly.1posix>.

- Set a read-only variable:

`readonly {{variable_name}}={{value}}`

- Mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint the names and values of all read-only variables to `stdout`:

`readonly -p`
