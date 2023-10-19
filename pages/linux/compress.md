# compress
> Compresses files using the Unix `compress` command. For more detailed information, please refer to the [compress manual page] <https://man7.org/linux/man-pages/man1/compress.1p.html>.

Compress Specific Files:
- `compress {{filename}}`

Compress Specific Files while Ignoring Nonexistent Ones:
- `compress -force {{filename}}`

Set Maximum Compression Bits (9-16 bits):
- `compress -b`
    
The -b flag sets compression bits (9-16) with a default of 16, starting at 9 bits and increasing as needed.    
Write to Standard Output (No Files Are Changed):
- `compress -c {{filename}}`

Decompress Files (Function Like uncompress):
- `compress -d {{filename}}`
   
Omit Compressed File Header:
- `compress -n {{filename}}`

Display Compression Percentage:
- `compress -v {{filename}}`.
