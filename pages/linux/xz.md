# xz

> Data compression software with a high compression ratio
> Can compress typical files ~30% smaller than gzip and ~15% smaller output than bzip2.
> Syntax is similar to that of gzip
> More information: <https://tukaani.org/xz/>.

- Compress a single file

`xz {{file}}`

- Compress multiple files

`xz {{file1}} {{file2}} {{file3}}`

- Decompress a file

`xz -d {{file.xz}}`

- Keep the input file (by default xz replaces the input file with the compressed/decompressed file)

`xz -k {{file}}`

- Write the compressed or decompressed data to standard output

`xz -cd {{file}}`

- Set the compression level (0 to 9, default is 6)

`xz {{-9}} {{file}}`
