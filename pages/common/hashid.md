# hashid

> Hashid is a python3 program that identifies data and password hashes.
> More information: <https://github.com/psypanda/hashID>.

- Identify hashes from standard input (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identify hashes passed as arguments (multiple hashes can be passed):

`hashid 72b302bf297a228a75730123efef7c41`

- Identify hashes on a file (one hash per line):

`hashid hashes.txt`

- Show all possible hash types (including salted hashes):

`hashid --extended 72b302bf297a228a75730123efef7c41`

- Show `hashcat`'s mode number and `john`'s format string of the hash types:

`hashid --mode --john 72b302bf297a228a75730123efef7c41`

- Save output to a file instead of printing to standard output:

`hashid --outfile hash_type.txt 72b302bf297a228a75730123efef7c41`
