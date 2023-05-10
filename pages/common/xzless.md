# xzless

> Display text from `.xz` and `.lzma` files.
> See also: `less`.
> More information: <https://manned.org/xzless>.

- View a compressed file:

`xzless {{path/to/archive.xz}}`

- View a compressed file [r]ecursively page by page:

`xzless -r {{path/to/archive.xz}}`

- View a compressed file and display the line [n]umber:

`xzless -N {{path/to/archive.xz}}`

- View a compressed file and [f]ollow it:

`xzless -F {{path/to/archive.xz}}`
