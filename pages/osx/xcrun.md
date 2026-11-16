# xcrun

> Run or locate development tools and properties.
> More information: <https://keith.github.io/xcode-man-pages/xcrun.1.html>.

- Find and run a tool from the active developer directory:

`xcrun {{tool}} {{arguments}}`

- Run a tool with verbose information about how it is located:

`xcrun --verbose {{tool}} {{arguments}}`

- Find the path to a tool for a given SDK:

`xcrun --sdk {{sdk_name}} --find {{tool}}`

- Find the path to a tool for a given toolchain:

`xcrun --toolchain {{name}} --find {{tool}}`

- Display help:

`xcrun --help`

- Display version:

`xcrun --version`
