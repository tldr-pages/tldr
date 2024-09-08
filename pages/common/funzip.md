# funzip

> Print the content of the first (non-directory) member in an archive without extraction.
> More information: <https://manned.org/funzip>.

- Print the content of the first member in a Zip archive:

`funzip {{path/to/archive.zip}}`

- Print the content in a gzip archive:

`funzip {{path/to/archive.gz}}`

- Decrypt a Zip or gzip archive and print the content:

`funzip -password {{password}} {{path/to/archive}}`
