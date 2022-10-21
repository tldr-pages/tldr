# funzip

> Print the content of the first (non-directory) member in an archive without extraction.
> More information: <https://manned.org/funzip>.

- Print the content of the first member in a `.zip` archive:

`funzip {{path/to/archive.zip}}`

- Decrypt a `.zip` or `.gz` archive and print the content:

`funzip -password {{password}} {{path/to/archive}}`
