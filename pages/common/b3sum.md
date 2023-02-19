# b3sum

> Command line utility for calculating BLAKE3 hashes.
> It is similar to Coreutils tools like b2sum or md5sum.
> More information: <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calculate the BLAKE3 checksum for a file:

`b3sum {{path/to/file}}`

- Calculate BLAKE3 checksums for multiple files:

`b3sum {{path/to/file1}} {{path/to/file2}}`

- Calculate the BLAKE3 checksum from `stdin`:

`{{some_command}} | b3sum`

- Create a file of BLAKE3 checksums:

`b3sum {{path/to/file}} > {{path/to/file.b3}}`

- Read and verify a file of BLAKE3 checksums:

`b3sum --check {{path/to/file.b3}}`
