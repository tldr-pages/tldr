# xattr

> Utility to work with extended filesystem attributes.
> More information: <https://ss64.com/osx/xattr.html>.

- List key:value extended attributes for a given file:

`xattr -l {{path/to/file}}`

- Write an attribute for a given file:

`xattr -w {{attribute_key}} {{attribute_value}} {{path/to/file}}`

- Delete an attribute from a given file:

`xattr -d {{com.apple.quarantine}} {{path/to/file}}`

- Delete all extended attributes from a given file:

`xattr -c {{path/to/file}}`

- Recursively delete an attribute in a given directory:

`xattr -rd {{attribute_key}} {{path/to/directory}}`
