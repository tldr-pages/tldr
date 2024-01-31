# rarcrack

> Password cracker for `rar`, `zip` and `7z` archives.

- Brute force the password for an archive (tries to guess the archive type):

`rarcrack {{path/to/file.zip}}`

- Specify the archive type:

`rarcrack --type {{rar|zip|7z}} {{path/to/file.zip}}`

- Use multiple threads:

`rarcrack --threads {{6}} {{path/to/file.zip}}`
