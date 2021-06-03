# 7zr

> File archiver with a high compression ratio.
> Similar to `7z` except that it only supports `.7z` files.
> More information: <https://www.7-zip.org>.

- [a]rchive a file or directory:

`7zr a {{path/to/archive.7z}} {{path/to/file_or_directory}}`

- Encrypt an existing archive (including file names):

`7zr a {{path/to/encrypted.7z}} -p{{password}} -mhe=on {{path/to/archive.7z}}`

- E[x]tract an archive preserving the original directory structure:

`7zr x {{path/to/archive.7z}}`

- E[x]tract an archive to a specific directory:

`7zr x {{path/to/archive.7z}} -o{{path/to/output}}`

- E[x]tract an archive to stdout:

`7zr x {{path/to/archive.7z}} -so`

- [l]ist the contents of an archive:

`7zr l {{path/to/archive.7z}}`

- List available archive types:

`7zr i`
