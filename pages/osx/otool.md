# otool

> Display specified parts of object files, libraries and executables.
> More information: <https://keith.github.io/xcode-man-pages/otool.1.html>.

- Display the shared libraries a binary is linked against:

`otool -L {{path/to/binary}}`

- Display the install name of a shared library:

`otool -D {{path/to/library.dylib}}`

- Display the Mach header:

`otool -h {{path/to/binary}}`

- Display the load commands:

`otool -l {{path/to/binary}}`

- Disassemble the text section, showing symbolic operands:

`otool -tV {{path/to/binary}}`

- Display the headers of a universal (fat) binary:

`otool -f {{path/to/binary}}`

- Display the contents of a specific section:

`otool -s {{__TEXT}} {{__cstring}} {{path/to/binary}}`

- Operate on one architecture within a universal binary:

`otool -arch {{arm64}} -L {{path/to/binary}}`
