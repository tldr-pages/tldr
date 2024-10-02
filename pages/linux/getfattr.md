# getfattr

> Display file names and extended attributes.
> More information: <https://manned.org/man/getfattr>.

- To retrieve all extended attributes of a file and display them in a detailed format:

`getfattr -d {{path/to/file}}`

- To get a specific attribute of a file:

`getfattr -n user.{{attribute_name}} {{path/to/file}}`