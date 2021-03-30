# sum

> Compute checksums and the number of blocks for a file.
> A predecessor to the more modern `cksum`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/sum-invocation.html>.

- Compute a checksum with BSD-compatible algorithm and 1024-byte blocks:

`sum {{file}}`

- Compute a checksum with System V-compatible algorithm and 512-byte blocks:

`sum --sysv {{file}}`
