# zip2john

> A tool to extract password hashes from zip files for use with John the Ripper password cracker.
> This is a utility tool usually installed as part of the John the Ripper installation.
> More information: <https://www.openwall.com/john/>.

- Extract the password hash from an archive, listing all files in the archive:

`zip2john {{path/to/file.zip}}`

- Extract the password has using [o]nly the specified file within the archive:

`zip2john -o {{compressed_file_in_zip}} {{path/to/file.zip}}`

- Output the extracted hash into a file so that it can be used with John the Ripper:

`zip2john -o {{compressed_file_in_zip}} {{path/to/file.zip}} > {{file.hash}}`
