# hashid

> hashid is a python3 program that identifies data and password hashes
> More information: <https://github.com/psypanda/hashID>.

- Identifies a hash from standard input (through typing, copying and pasting, or piping the hash into the program):

`hashid`

- Identifies hashes passed as arguments (multiple hashes can be passed):

`hashid 72b302bf297a228a75730123efef7c41`

- Identifies hashes from a file (one hash per line):

`hashid hashes.txt`

- Shows all possible hash types (even salted hashes):

`hashid --extended 72b302bf297a228a75730123efef7c41`

- Shows the hash types' `hashcat`'s mode number and `john`'s format string:

`hashid --mode --john 72b302bf297a228a75730123efef7c41`

- Saves output to a file instead of printing to standard output:

`hashid --outfile hash_type.txt 72b302bf297a228a75730123efef7c41`
