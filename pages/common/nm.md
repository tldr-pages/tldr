# nm

> List symbol names in object files.
> More information: <https://manned.org/nm>.

- List global (extern) functions in a file (prefixed with T):

`nm --extern-only {{path/to/file.o}}`

- List only undefined symbols in a file:

`nm --undefined-only {{path/to/file.o}}`

- List all symbols, even debugging symbols:

`nm --debug-syms {{path/to/file.o}}`

- Demangle C++ symbols (make them readable):

`nm --demangle {{path/to/file.o}}`
