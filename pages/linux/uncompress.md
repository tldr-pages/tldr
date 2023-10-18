# uncompress

> Uncompress the  files 
See also: uncompress
More information: <https://man7.org/linux/man-pages/man1/uncompress.1p.html>

- Uncompress the specific files:

`Uncompress [*file*...]`

- Uncompress specific files ignoring nonexistent ones:

`uncompress [-f] [*file*...]`

- Writes to the standard output; no files are changed and no **.Z** files are created. The behavior of **[zcat](https://www.computerhope.com/unix/uzcat.htm)** is identical to that of "**uncompress -c**"

`uncompress [-c] [*file*...]`

- [Verbose](https://www.computerhope.com/jargon/v/verbose.htm). Writes to standard error any messages concerning the percentage reduction or expansion of each file

`uncompress [-v] [*file*...]`

- Sets the upper limit (in [bits](https://www.computerhope.com/jargon/b/bit.htm)) for common [substring](https://www.computerhope.com/jargon/s/substring.htm) codes. Bits must be between **9** and **16** (**16** is the default). Lowering the number of bits results in larger, less-compressed files

`uncompress [-b] [*file*...]`
