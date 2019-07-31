# mat2

> Anonymise various file formats by removing metadata.
> More information: <https://0xacab.org/jvoisin/mat2>.

- List supported file formats:

`mat2 --list`

- Remove metadata from a file:

`mat2 {{path/to/file}}`

- Remove metadata from a file and print detailed output to the console:

`mat2 --verbose {{file_path}}`

- Show metadata in a file without removing it:

`mat2 --show {{file_path}}`

- Partially remove metadata from a file:

`mat2 --lightweight {{file_path}}`
