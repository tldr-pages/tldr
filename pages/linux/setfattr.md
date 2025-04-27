# setfattr

> Set extended file attributes.
> More information: <https://manned.org/setfattr>.

- Set name of attribute for file:

`setfattr {{[-n|--name]}} user.{{attribute_name}} {{path/to/file}}`

- Set a user-defined value of an extended attribute on a file:

`setfattr {{[-n|--name]}} user.{{attribute_name}} {{[-v|--value]}} "{{value}}" {{path/to/file}}`

- Remove a specific attribute of a file:

`setfattr {{[-x|--remove]}} user.{{attribute_name}} {{path/to/file}}`
