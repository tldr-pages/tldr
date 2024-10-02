# setfattr

> Set extended file attributes.
> More information: <https://manned.org/man/setfattr>.

- Set name of attribute for file:

`setfattr -n user.{{attribute_name}} {{path/to/file}}`

- Set a user-defined value of an extended attribute on a file:

`setfattr -n user.{{attribute}} -v "{{value}}" {{path/to/file}}`

- Remove a specific attribute of a file:

`setfattr -x user.{{attribute}} {{path/to/file}}`
