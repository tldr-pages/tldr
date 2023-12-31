# readonly

> Set read-only shell variables.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#readonly>.

- Create a read-only variable:

`readonly {{variable_name}}={{value}}`

- Mark a variable as read-only:

`readonly {{existing_variable}}`

- [p]rint the names and values of all read-only variables to `stdout`:

`readonly -p`
