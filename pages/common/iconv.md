# iconv

> Converts text from one encoding to another.

- Convert file and print to stdout:

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Convert file to current locale:

`iconv -f {{from_encoding}} {{input_file}} > {{output_file}}`

- List supported encodings:

`iconv -l`
