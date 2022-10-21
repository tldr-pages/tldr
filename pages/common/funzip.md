# funzip

> Print the content of the first (non-directory) member in an archive without extraction.
> More information: <https://manned.org/funzip>.

- Print the content of the first member in a `.zip` archive:

`funzip {{path/to/archive.zip}}`

- Print the content in a `.gz` archive:

`funzip {{path/to/archive.gz}}`

- Decrypt a `.zip` or `.gz` archive and print the content:

`funzip -password {{password}} {{path/to/archive}}`
