# ldd

> Display shared library dependencies of a binary.
> Do not use on an untrusted binary, use objdump for that instead.
> More information: <https://manned.org/ldd>.

- Display shared library dependencies of a binary:

`ldd {{path/to/binary}}`

- Display all information about dependencies:

`ldd {{[-v|--verbose]}} {{path/to/binary}}`

- Display unused direct dependencies:

`ldd {{[-u|--unused]}} {{path/to/binary}}`

- Report missing data objects and perform data relocations:

`ldd {{[-d|--data-relocs]}} {{path/to/binary}}`

- Report missing data objects and functions, and perform relocations for both:

`ldd {{[-r|--function-relocs]}} {{path/to/binary}}`
