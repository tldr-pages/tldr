# shasum

> Calculate SHA cryptographic checksums.
> More information: <https://manned.org/shasum>.

- Calculate the SHA1 checksum for one or more files:

`shasum {{path/to/file1 path/to/file2 ...}}`

- Calculate the SHA checksum for one or more files with the specified algorithm:

`shasum --algorithm {{1|224|256|384|512|512224|512256}} {{path/to/file1 path/to/file2 ...}}`

- Calculate a SHA1 checksum from `stdin`:

`{{command}} | shasum`

- Calculate and save the list of SHA256 checksums to a file:

`shasum --algorithm 256 {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha256}}`

- Read a file of SHA checksums and filenames and verify all files have matching checksums (the algorithm will be automatically detected):

`shasum {{[-c|--check]}} {{path/to/file}}`

- Only show a message for missing files or when verification fails:

`shasum {{[-c|--check]}} --quiet {{path/to/file}}`

- Only show a message when verification fails, ignoring missing files:

`shasum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file}}`

- Check a known SHA checksum of a file:

`echo {{known_sha_checksum_of_the_file}} {{path/to/file}} | shasum {{[-c|--check]}}`
