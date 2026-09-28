# vcpkg hash

> Compute the hash of a file.
> More information: <https://learn.microsoft.com/en-us/vcpkg/commands/hash>.

- Compute the SHA-512 hash of a file:

`vcpkg hash {{path/to/file}}`

- Compute the hash of a file using a specific algorithm (`sha512` or `sha256`):

`vcpkg hash {{path/to/file}} {{sha256}}`
