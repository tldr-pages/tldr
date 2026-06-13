# lzop

> Compress or decompress files with LZO compression.
> More information: <https://www.lzop.org/lzop_man.php>.

- Compress a file into a new file with the `.lzo` suffix:

`lzop {{path/to/file}}`

- Decompress a file:

`lzop {{[-d|--decompress]}} {{path/to/file.lzo}}`

- Compress a file, while specifying the compression level. 0 = Worst, 9 = Best (Default level is 3):

`lzop -{{level}} {{path/to/file}}`

- Compress a file with the best compression level:

`lzop {{[-9|--best]}} {{path/to/file}}`

- Compress a file with the fastest compression level:

`lzop {{[-1|--fast]}} {{path/to/file}}`
