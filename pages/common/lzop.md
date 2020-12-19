# lzop

> Compress or decompress files with LZO compression.
> More information: <https://www.lzop.org/>.

- Compress a file into a new file with the .lzo suffix:

`lzop {{file}}`

- Decompress a file:

`lzop -d {{file}}.lzo`

- Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):

`lzop -{{level}} {{file}}`
