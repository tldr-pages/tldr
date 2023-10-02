# readonly

> Create or modify read-only variables within a shell script, preventing the variable changed by subsequent commands.
> This is useful when you want to ensure that a variable retains a constant value throughout the execution of a script.
> More information: <https://manned.org/readonly.1p>.

- To create a read-only variable:

`readonly {{variable_name}}={{value}}`

- To mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint to the standard output the names and values of all read-only variables:

`readonly -p`
