# zip2john

> A tool to extract password hashes from `zip` archives for use with John the Ripper password cracker.
> This is a utility tool usually installed as part of the John the Ripper installation.
> More information: <https://www.openwall.com/john/>.

- Extract the password hash from an archive, listing all files in the archive:

`zip2john {{path/to/file.zip}}`

- Extract the password hash using [o]nly a specific compressed file:

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}}`

- Extract the password hash from a compressed file to a specific file (for use with John the Ripper):

`zip2john -o {{path/to/compressed_file}} {{path/to/file.zip}} > {{file.hash}}`
