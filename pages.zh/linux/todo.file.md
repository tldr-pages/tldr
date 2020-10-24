# file

> Determine file type.

- Give a description of the type of the specified file. Works fine for files with no file extension:

`file {{filename}}`

- Look inside a zipped file and determine the file type(s) inside:

`file -z {{foo.zip}}`

- Allow file to work with special or device files:

`file -s {{filename}}`

- Don't stop at first file type match; keep going until the end of the file:

`file -k {{filename}}`

- Determine the mime encoding type of a file:

`file -i {{filename}}`
