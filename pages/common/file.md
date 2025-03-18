# file

> Determine file type.
> More information: <https://manned.org/file>.

- Give a description of the type of the specified file. Works fine for files with no file extension:

`file {{path/to/file}}`

- Look inside a zipped file and determine the file type(s) inside:

`file {{[-z|--uncompress]}} {{foo.zip}}`

- Allow file to work with special or device files:

`file {{[-s|--special-files]}} {{path/to/file}}`

- Don't stop at first file type match; keep going until the end of the file:

`file {{[-k|--keep-going]}} {{path/to/file}}`

- Determine the MIME encoding type of a file:

`file {{[-i|--mime]}} {{path/to/file}}`
