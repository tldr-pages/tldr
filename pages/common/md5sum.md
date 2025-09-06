# md5sum

> Calculate MD5 cryptographic checksums.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/md5sum-invocation.html>.

- Calculate the MD5 checksum for one or more files:

`md5sum {{path/to/file1 path/to/file2 ...}}`

- Calculate and save the list of MD5 checksums to a file:

`md5sum {{path/to/file1 path/to/file2 ...}} > {{path/to/file.md5}}`

- Calculate an MD5 checksum from `stdin`:

`{{command}} | md5sum`

- Read a file of MD5 checksums and filenames and verify all files have matching checksums:

`md5sum {{[-c|--check]}} {{path/to/file.md5}}`

- Only show a message for missing files or when verification fails:

`md5sum {{[-c|--check]}} --quiet {{path/to/file.md5}}`

- Only show a message when verification fails, ignoring missing files:

`md5sum --ignore-missing {{[-c|--check]}} --quiet {{path/to/file.md5}}`

- Check a known MD5 checksum of a file:

`echo {{known_md5_checksum_of_the_file}} {{path/to/file}} | md5sum {{[-c|--check]}}`
