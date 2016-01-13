# nm

> List symbol names in object files (see c++filt).

- List global (extern) functions in a file (prefixed with T:

`nm -g {{file.o}}`

- List only undefined symbols in a fil:

`nm -u {{file.o}}`

- List all symbols, even debugging symbol:

`nm -a {{file.o}}`
