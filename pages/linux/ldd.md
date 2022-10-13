# ldd

> Display shared library dependencies of a binary.
> Do not use on an untrusted binary, use objdump for that instead.
> More information: <https://manned.org/ldd>.

- Display shared library dependencies of a binary:

`ldd {{path/to/binary}}`

- Display _all_ information about dependencies:

`ldd --verbose {{path/to/binary}}`

- Display unused direct dependencies:

`ldd --unused {{path/to/binary}}`

- Report missing data objects and perform data relocations (ELF ONLY):

`ldd --data-relocs {{path/to/binary}}`

- Report missing data objects and functions, and perform relocations for both (ELF ONLY):

`ldd --function-relocs {{path/to/binary}}`
