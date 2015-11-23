# iconv

> Converts text from one encoding to another

- convert file and print to stdout

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- convert multiple files

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file1}} {{input_file2}} > {{output_file}}`

- convert file to current locale

`iconv -f {{from_encoding}} {{input_file}} > {{output_file}}`

- list supported encodings

`iconv -l`
