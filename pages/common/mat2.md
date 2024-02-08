# mat2

> Anonymise various file formats by removing metadata.
> More information: <https://0xacab.org/jvoisin/mat2>.

- List supported file formats:

`mat2 --list`

- Remove metadata from a file:

`mat2 {{path/to/file}}`

- Remove metadata from a file and print detailed output to the console:

`mat2 --verbose {{path/to/file}}`

- Show metadata in a file without removing it:

`mat2 --show {{path/to/file}}`

- Partially remove metadata from a file:

`mat2 --lightweight {{path/to/file}}`

- Remove metadata from a file in place, without creating a backup:

`mat2 --inplace {{path/to/file}}`
