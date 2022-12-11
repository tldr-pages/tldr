# shasum

> Calculate or check cryptographic SHA checksums.
> More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for a file:

`shasum {{path/to/file}}`

- Calculate the SHA256 checksum for a file:

`shasum --algorithm 256 {{path/to/file}}`

- Calculate the SHA512 checksum for multiple files:

`shasum --algorithm 512 {{path/to/file1}} {{path/to/file2}}`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 {{path/to/file1}} {{path/to/file2}} > {{path/to/file.sha256}}`

- Check a file with a list of sums against the directory's files:

`shasum --check {{path/to/file}}`

- Check a list of sums and only show a message for files for which verification fails:

`shasum --check --quiet {{path/to/file}}`

- Calculate the SHA1 checksum from `stdin`:

`{{some_command}} | shasum`
