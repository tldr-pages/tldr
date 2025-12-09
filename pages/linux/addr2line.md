# addr2line

> Convert addresses of a binary into file names and line numbers.
> More information: <https://manned.org/addr2line>.

- Display the filename and line number of the source code from an instruction address of an executable:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{address}}`

- Display the function name, filename and line number:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{[-f|--functions]}} {{address}}`

- Demangle the function name for C++ code:

`addr2line {{[-e|--exe]}} {{path/to/executable}} {{[-f|--functions]}} {{[-C|--demangle]}} {{address}}`
