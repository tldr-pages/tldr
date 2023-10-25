# readonly

> Create or modify read-only variables within a shell script, preventing the variable from being changed by subsequent commands.
> This is useful when you want to ensure that a variable retains a constant value throughout the execution of a script.
> More information: <https://manned.org/readonly.1p>.

- Create a read-only variable:

`readonly {{variable_name}}={{value}}`

- Mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint the names and values of all read-only variables to `stdout`:

`readonly -p`
