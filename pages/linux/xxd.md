# xxd

> Make a Hex dump or do the reverse.
> More information: <https://packages.debian.org/buster/xxd>.

- Display Hex representation of a file:

`xxd {{file}}`

- Convert a Hex dump into binary:

`xxd -r {{path/to/file}}`

- Produce a binary dump:

`xxd -b {{path/to/file}}`

- Print everything but the first three lines (hex  0x30  bytes):

`xxd -s 0x30 {{path/to/file}}`

- Print 120 bytes as continuous hexdump with 20 octets per line:

`xxd -l {{120}} -ps -c {{20}} {{path/to/file}}`
