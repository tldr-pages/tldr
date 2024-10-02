# setfattr

> Set extended file attributes.
> More information: <https://manned.org/man/setfattr>.

- To set name of attribute for file:

`setfattr -n user.{{attribute_name}} {{path/to/file}}`

- To set a user-defined value of an extended attribute on a file:

`setfattr -n user.{{attribute}} -v "{{value}}" {{path/to/file}}`

- To remove a specific attribute of a file:

`setfattr -x user.{{attribute}} {{path/to/file}}`
