# xzless

> Display text from `.xz` and `.lzma` files.
> See also: `less`.
> More information: <https://manned.org/xzless>.

- View a compressed file:

`xzless {{path/to/archive}}`

- View a compressed file and display line numbers:

`xzless --LINE-NUMBERS {{path/to/archive}}`

- View a compressed file and quit if the entire file can be displayed on the first screen:

`xzless --quit-if-one-screen {{path/to/archive}}`
