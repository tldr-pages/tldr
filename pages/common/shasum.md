# shasum

> Calculate SHA cryptographic checksums.
> More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for one or more files:

`shasum {{path/to/file1 path/to/file2 ...}}`

- Calculate the SHA256 checksum for one or more files:

`shasum --algorithm 256 {{path/to/file1 path/to/file2 ...}}`

- Calculate the SHA512 checksum for one or more files:

`shasum --algorithm 512 {{path/to/file1 path/to/file2 ...}}`

- Calculate a SHA1 checksum from `stdin`:

`{{command}} | shasum`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha256}}`

- Read a file of SHA1 sums and filenames and verify all files have matching checksums:

`shasum --check {{path/to/file}}`

- Only show a message for missing files or when verification fails:

`shasum --check --quiet {{path/to/file}}`

- Only show a message when verification fails, ignoring missing files:

`shasum --ignore-missing --check --quiet {{path/to/file}}`
