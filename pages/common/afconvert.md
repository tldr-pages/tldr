# afconvert

> Convert between AFF and raw file formats.
> More information: <https://manned.org/afconvert.1>.

- Use a specific extension (default: `aff`):

`afconvert -a {{extension}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`

- Use a specific compression level (default: `7`):

`afconvert -X{{0..7}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`
