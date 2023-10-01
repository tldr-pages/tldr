# readonly

> In Linux, the readonly command is used to create or modify read-only variables within a shell script.
> When a variable is marked as read-only using readonly, its value cannot be changed or modified by subsequent commands within the script.
> This can be useful when you want to ensure that a variable retains a constant value throughout the execution of a script.
> More information: <https://manned.org/readonly.1p>.

- To create a read-only variable:

`readonly {{variable_name}}={{value}}`

- To mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint to the standard output the names and values of all read-only variables:

`readonly -p`
