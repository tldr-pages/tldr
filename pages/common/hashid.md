# hashid

> Python3 program that identifies data and password hashes.
> More information: <https://github.com/psypanda/hashID#usage>.

- Identify hashes from `stdin` (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identify one or more hashes:

`hashid {{hash1 hash2 ...}}`

- Identify hashes on a file (one hash per line):

`hashid {{path/to/hashes.txt}}`

- Show all possible hash types (including salted hashes):

`hashid {{[-e|--extended]}} {{hash}}`

- Show `hashcat`'s mode number and `john`'s format string of the hash types:

`hashid {{[-m|--mode]}} {{[-j|--john]}} {{hash}}`

- Save output to a file instead of printing to `stdout`:

`hashid {{[-o|--outfile]}} {{path/to/output.txt}} {{hash}}`
