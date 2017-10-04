# shasum

> Calculate or check cryptographic SHA checksums.

- Calculate the SHA1 checksum for a file:

`shasum {{filename}}`

- Calculate the SHA256 checksum for a file:

`shasum -a 256 {{filename}}`

- Calculate the SHA512 checksum for multiple files:

`shasum -a 512 {{filename1}} {{filename2}}`

- Check a file with a list of sums against the directorys files:

`shasum -c {{list_file}}`

- Calculate the SHA1 checksum from stdin:

`{{somecommand}} | shasum`
