# shasum

> Calculate or check cryptographic SHA checksums.

- Calculate the SHA1 checksum for a file:

`shasum {{filename}}`

- Calculate the SHA256 checksum for a file:

`shasum --algorithm 256 {{filename}}`

- Calculate the SHA512 checksum for multiple files:

`shasum --algorithm 512 {{filename1}} {{filename2}}`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 {{filename1}} {{filename2}} > {{filename.sha256}}`

- Check a file with a list of sums against the directory's files:

`shasum --check {{list_file}}`

- Check a list of sums and only show a message for files for which verification fails:

`shasum --check --quiet {{list_file}}`

- Calculate the SHA1 checksum from `stdin`:

`{{somecommand}} | shasum`
