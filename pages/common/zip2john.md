# zip2john

> A tool to extract password hashes from zip files for use with John the Ripper password cracker.
> This is a utility tool usually installed as part of the John the Ripper installation.

- Extract the password hash from an archive, will list all files in the archive:

`zip2john {{file.zip}}`

- Extract the password has using [o]nly the specified file within the archive:

`zip2john -o {{compressed_file_in_zip}} {{file.zip}}`

- Output the extracted hash into a file so that it can be used with John the Ripper:

`zip2john -o {{compressed_file_in_zip}} {{file.zip}} > {{file.hash}}`
