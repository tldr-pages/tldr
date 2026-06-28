# attr

> Manipulate extended attributes on filesystem objects.
> More information: <https://manned.org/attr>.

- List the names and sizes of all extended attributes of a file:

`attr -l {{path/to/file}}`

- Get the value of an extended attribute:

`attr -g {{attribute_name}} {{path/to/file}}`

- Set an extended attribute value:

`attr -s {{attribute_name}} -V "{{attribute_value}}" {{path/to/file}}`

- Set an extended attribute using a value from `stdin`:

`echo "{{attribute_value}}" | attr -s {{attribute_name}} {{path/to/file}}`

- Remove an extended attribute:

`attr -r {{attribute_name}} {{path/to/file}}`
