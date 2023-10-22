# lzop

> Compress or decompress files with LZO compression.
> More information: <https://www.lzop.org/>.

- Compress a file into a new file with the `.lzo` suffix:

`lzop {{path/to/file}}`

- Decompress a file:

`lzop -d {{path/to/file}}.lzo`

- Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):

`lzop -{{level}} {{path/to/file}}`
