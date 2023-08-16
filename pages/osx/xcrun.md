# xcrun

> Run or locate development tools and properties.
> More information: <https://www.unix.com/man-page/osx/1/xcrun/>.

- Find and run a tool from the active developer directory:

`xcrun {{tool}} {{arguments}}`

- Show verbose output:

`xcrun {{tool}} {{arguments}} --verbose`

- Find a tool for a given SDK:

`xcrun --sdk {{sdk_name}}`

- Find a tool for a given toolchain:

`xcrun --toolchain {{name}}`

- Display version:

`xcrun --version`

- Display help:

`xcrun --help`
