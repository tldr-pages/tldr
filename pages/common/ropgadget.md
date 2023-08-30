# ROPgadget

> Find ROP gadgets in binary files.
> More information: <https://github.com/JonathanSalwan/ROPgadget>.

- List gadgets in the binary file:

`ROPgadget --binary {{path/to/binary}}`

- Filter gadgets in the binary file by a regular expression:

`ROPgadget --binary {{path/to/binary}} --re {{regex}}`

- List gadgets in the binary file, excluding specified type:

`ROPgadget --binary {{path/to/binary}} --{{norop|nojob|nosys}}`

- Exclude bad byte gadgets in the binary file:

`ROPgadget --binary {{path/to/binary}} --badbytes {{byte_string}}`

- List gadgets up to the specified number of bytes in the binary file:

`ROPgadget --binary {{path/to/binary}} --depth {{nbyte}}`
