# md5sum

> Compute and check MD5 message digest.
> More information: <https://manpages.debian.org/bullseye/coreutils/md5sum.1.en.html>.

- Print or check MD5(128-bit) checksum:

`md5sum {{file}}`

- Store the MD5 checksum in file:

`md5sum {{path_to_file}} > {{saved_hash.md5}}`

- Check if the files saved still match with the hashes:

`md5sum -c {{saved_hash.md5}}`
