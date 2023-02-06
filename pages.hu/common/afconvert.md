# afconvert

> Konvertálás AFF és nyers fájlformátumok között. További információ: <https://manned.org/afconvert.1>.

- Egy adott kiterjesztés használata (alapértelmezett: `aff`):

`afconvert -a {{extension}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`

- Egy adott tömörítési szint használata (alapértelmezett: `7`):

`afconvert -X{{0..7}} {{path/to/input_file}} {{path/to/output_file1 path/to/output_file2 ...}}`
