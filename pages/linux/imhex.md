# imhex

> Hex editor for reverse engineers and programmers.
> More information: <https://docs.werwolv.net/imhex/>.

- Open a file in ImHex:

`imhex {{path/to/file}}`

- Create a new empty file:

`imhex --new`

- Open a file in the currently running ImHex instance and select a range of bytes (offsets in hexadecimal):

`imhex --open {{path/to/file}} --select {{0xstart_offset}} {{0xend_offset}}`

- Display information about a file:

`imhex --file-info {{path/to/file}}`

- Calculate the hash of a file using a specific algorithm (`md5`, `sha1`, `sha224`, `sha256`, `sha384`, `sha512`):

`imhex --hash {{algorithm}} {{path/to/file}}`

- Generate a hex dump of a file:

`imhex --hexdump {{path/to/file}}`

- Display version:

`imhex --version`
