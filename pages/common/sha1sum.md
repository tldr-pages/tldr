# sha1sum

> Calculate SHA1 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sha1sum-invocation.html>.

- Calculate the SHA1 checksum for one or more files:

`sha1sum {{path/to/file1 path/to/file2 ...}}`

- Calculate and save the list of SHA1 checksums to a file:

`sha1sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.sha1}}`

- Calculate a SHA1 checksum from `stdin`:

`{{command}} | sha1sum`

- Read a file of SHA1 checksums and filenames and verify all files have matching checksums:

`sha1sum {{[-c|--check]}} {{path/to/file.sha1}}`

- Only show a message for missing files or when verification fails:

`sha1sum {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- Only show a message when verification fails, ignoring missing files:

`sha1sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.sha1}}`

- Check a known SHA1 checksum of a file:

`echo {{known_sha1_checksum_of_the_file}} {{path/to/file}} | sha1sum {{[-c|--check]}}`
