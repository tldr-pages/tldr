# compress
> Compresses files using the Unix `compress` command. More details: <https://man7.org/linux/man-pages/man1/compress.1p.html>.

Compress Specific Files:
- `compress {{filename}}`

Compress Specific Files, Ignore Nonexistent Ones:
- `compress --force {{filename}}`

Set Maximum Compression Bits (9-16 bits):
- `compress -b`: Max bits 9-16, default 16, starting at 9 and increasing as needed.

Write to Standard Output (No Files Are Changed):
- `compress -c {{filename}}`

Decompress Files (Functions Like uncompress):
- `compress -d {{filename}}`

Omit Compressed File Header:
- `compress -n {{filename}}`

Display Compression Percentage:
- `compress -v {{filename}}`
