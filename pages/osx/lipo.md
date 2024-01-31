# lipo

> Tool for handling Mach-O Universal Binaries.
> More information: <https://keith.github.io/xcode-man-pages/lipo.1.html>.

- Create a universal file from two single-architecture files:

`lipo {{path/to/binary_file.x86_64}} {{path/to/binary_file.arm64e}} -create -output {{path/to/binary_file}}`

- List all architectures contained in a universal file:

`lipo {{path/to/binary_file}} -archs`

- Display detailed information about a universal file:

`lipo {{path/to/binary_file}} -detailed_info`

- Extract a single-architecture file from a universal file:

`lipo {{path/to/binary_file}} -thin {{arm64e}} -output {{path/to/binary_file.arm64e}}`
