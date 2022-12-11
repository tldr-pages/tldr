# file

> Determine file type.
> More information: <https://manned.org/file>.

- Give a description of the type of the specified file. Works fine for files with no file extension:

`file {{path/to/file}}`

- Look inside a zipped file and determine the file type(s) inside:

`file -z {{foo.zip}}`

- Allow file to work with special or device files:

`file -s {{path/to/file}}`

- Don't stop at first file type match; keep going until the end of the file:

`file -k {{path/to/file}}`

- Determine the MIME encoding type of a file:

`file -i {{path/to/file}}`
