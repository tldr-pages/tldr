# strings

> Find printable strings in an object file or binary.
> More information: <https://manned.org/strings>.

- Print all strings in a binary:

`strings {{path/to/file}}`

- Limit results to strings at least *length* characters long:

`strings -n {{length}} {{path/to/file}}`

- Prefix each result with its offset within the file:

`strings -t d {{path/to/file}}`

- Prefix each result with its offset within the file in hexadecimal:

`strings -t x {{path/to/file}}`
