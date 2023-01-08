# unzstd

> Decompress files with Zstandard compression.
> More information: <https://github.com/facebook/zstd>.

- Decompress files:

`unzstd {{path/to/file1.ztd path/to/file2.ztd ...}}`

- Decompress a file into a specific output file:

`unzstd {{path/to/compressed.ztd}} -o {{path/to/extracted_file}}`

- Display information about a compressed file:

`unzip --list {{path/to/file.zst}}`
