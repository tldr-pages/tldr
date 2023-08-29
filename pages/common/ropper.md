# ropper

> Find ROP gadgets in binary files.
> More information: <http://scoding.de/ropper/>.

- List gadgets in the binary file:

`ropper --file {{path/to/binary}}`

- List gadgets in the binary file, filtered by regular expression:

`ropper --file {{path/to/binary}} --search {{regex}}`

- List gadgets in the binary file of the specified type:

`ropper --file {{path/to/binary}} --type {{rop|job|sys|all}}`

- List gadgets in the binary file, not including bad bytes:

`ropper --file {{path/to/binary}} --badbytes {{byte_string}}`

- List gadgets in the binary file, with up to the given instructions count:

`ropper --file {{path/to/binary}} --inst-count {{count}}`
