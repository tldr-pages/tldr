# # compress
> Compresses files using the Unix `compress` command. For more detailed information, please refer to the [compress manual page] <https://man7.org/linux/man-pages/man1/compress.1p.html>.

**Compress Specific Files:**

- `compress {{filename}}`

**Compress Specific Files while Ignoring Nonexistent Ones:**

- `compress --force {{filename}}`

**Set Maximum Compression Bits (9-16 bits):**

- `compress -b`
    
The `-b` flag specifies the maximum number of bits to use when replacing common substrings in the file. It must be in the range of 9 to 16 bits, with the default being 16 bits. The algorithm initially uses 9-bit codes and progresses to higher bit codes until the limit is reached.
    
**Write to Standard Output (No Files Are Changed):**

- `compress -c {{filename}}`

**Decompress Files (Function Like uncompress):**

- `compress -d {{filename}}`
   
**Omit Compressed File Header:**

- `compress -n {{filename}}`

**Display Compression Percentage:**

- `compress -v {{filename}}`
