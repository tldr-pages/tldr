# lzip

> Lzip is a lossless data compressor with a user interface similar to the one of gzip or bzip2.
Lzip uses a simplified form of the "Lempel-Ziv-Markovchain-Algorithm"z (LZMA) stream format and provides a 3 factor integrity checking to maximize interoperability and optimize safety.
> More information: <https://www.nongnu.org/lzip>.

- Archive a file, replacing it with an lzipped compressed version:

`lzip {{path/to/file}}`

- Archive a file keeping the input file:

`lzip -k {{path/to/file}}`

- Archive a file with best compression (level=9):

`lzip -k {{path/to/file}} --best`

- Archive a file at the fastest speed (level=0): 

`lzip -k {{path/to/file}} --fast`

- Test integrity of compressed file:

`lzip --test {{compressed.ext}}.lz`

- Decompress a file, replacing it with the original uncompressed version:

`lzip -d {{compressed.ext}}.lz`

- Decompress a file keeping the input file:

`lzip -d -k {{compressed.ext}}.lz`

- List files of archive and compression stats:

`lzip --list {{compressed.ext}}.lz`
