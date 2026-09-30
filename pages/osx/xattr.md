# xattr

> Display and manipulate the extended attributes of files and directories.
> More information: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

- List the names of all extended attributes of a file:

`xattr {{path/to/file}}`

- Print the value of a specific attribute:

`xattr -p {{com.apple.quarantine}} {{path/to/file}}`

- Remove a specific attribute (e.g. clear the Gatekeeper quarantine flag from a downloaded app):

`xattr -d {{com.apple.quarantine}} {{path/to/file}}`

- Remove all extended attributes from a file:

`xattr -c {{path/to/file}}`

- Recursively remove an attribute from all files in a directory:

`xattr -r -d {{com.apple.quarantine}} {{path/to/directory}}`

- Write an attribute value to a file:

`xattr -w {{attribute_name}} {{value}} {{path/to/file}}`
