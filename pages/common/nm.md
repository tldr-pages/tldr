# nm

> List symbol names in object files.
> More information: <https://manned.org/nm>.

- List global (extern) functions in a file (prefixed with T):

`nm {{[-g|--extern-only]}} {{path/to/file.o}}`

- List only undefined symbols in a file:

`nm {{[-u|--undefined-only]}} {{path/to/file.o}}`

- List all symbols, even debugging symbols:

`nm {{[-a|--debug-syms]}} {{path/to/file.o}}`

- Demangle C++ symbols (make them readable):

`nm {{[-C|--demangle]}} {{path/to/file.o}}`
