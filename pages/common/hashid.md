# hashid

> Python3 program that identifies data and password hashes.
> More information: <https://github.com/psypanda/hashID>.

- Identify hashes from `stdin` (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identify hashes passed as arguments (multiple hashes can be passed):

`hashid {{hash}}`

- Identify hashes on a file (one hash per line):

`hashid {{path/to/hashes.txt}}`

- Show all possible hash types (including salted hashes):

`hashid --extended {{hash}}`

- Show `hashcat`'s mode number and `john`'s format string of the hash types:

`hashid --mode --john {{hash}}`

- Save output to a file instead of printing to `stdout`:

`hashid --outfile {{path/to/output.txt}} {{hash}}`
