# convmv

> Converts filenames from one encoding to another

- convert encoding, dry run (without actually changes filename)

`convmv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- convert encoding, not dry run (actually rename the file)

`convmv -f {{from_encoding}} -t {{to_encoding}} --notest {{input_file}}`
