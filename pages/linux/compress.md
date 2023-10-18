# compress

> Compress the  files 
See also: compress
> More information: <https://man7.org/linux/man-pages/man1/compress.1p.html>.

- Compress the specific files:

`compress filename`

- Compress specific files ignoring nonexistent ones:

`compress --force filename`

- Compress file with Specifies the maximum number of bits to use to replace common substrings in the file. The value of the Bits variable must be in the range from 9 bits through 16 bits, with the default being 16 bits. When compressing data, the algorithm first uses all of the 9-bit codes (257 through 512) to replace as many substrings as possible. Then it uses all 10-bit codes, and so on, continuing until the limit specified by the -b flag is reached:

`compress -b`

- Writes to standard output. No files are changed:

`compress -c filename`

- Causes the compress command to function exactly like the uncompress command :

`compress -d filename`

- Omits the compressed file header from the compressed file :

`compress -n filename`

- Writes the percentage of compression :
  
`compress -v filename`
