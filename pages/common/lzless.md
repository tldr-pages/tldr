# lzless

> View the contents of compressed files page by page, using the `less` utility.
> More information: <https://manned.org/lzless>.

- View a compressed file page by page:

`lzless {{file.lzma}}`

- View a compressed file [r]ecursively page by page:

`lzless -r {{path/to/directory}}/*.lzma`

- View a compressed file and display the line [n]umber:

`lzless -N {{file.lzma}}`

- View a compressed file and [f]ollow it:

`lzless -F {{file.lzma}}`
