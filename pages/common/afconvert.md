# afconvert

> Convert between AFF and raw file formats.
> More information: <https://manned.org/afconvert.1>.

- Use a specific extension (default: `aff`):

`afconvert -a {{extension}} {{path/to/file}} {{path/to/file1 path/to/file2 ...}}`

- Use a specific compression level (default: `7`):

`afconvert -X{{0..7}} {{path/to/file}} {{path/to/file1 path/to/file2 ...}}`
