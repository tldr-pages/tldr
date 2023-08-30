# ropper

> Find ROP gadgets in binary files.
> More information: <http://scoding.de/ropper/>.

- List gadgets in the binary file:

`ropper --file {{path/to/binary}}`

- Filter gadgets in the binary file by a regular expression:

`ropper --file {{path/to/binary}} --search {{regex}}`

- List gadgets of specified type in the binary file:

`ropper --file {{path/to/binary}} --type {{rop|job|sys|all}}`

- Exclude bad byte gadgets in the binary file:

`ropper --file {{path/to/binary}} --badbytes {{byte_string}}`

- List gadgets up to the specified instruction count in the binary file:

`ropper --file {{path/to/binary}} --inst-count {{count}}`
