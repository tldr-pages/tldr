# convmv

> Convert filenames (NOT file content) from one encoding to another.

- Test filename encoding conversion (don't actually change the filename):

`convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Convert filename encoding and rename the file to the new enconding:

`convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}`
