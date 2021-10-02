# fscrypt

> Go tool for managing Linux filesystem encryption.
> More information: <https://github.com/google/fscrypt>.

- Prepare the root filesystem for use with fscrypt:

`fscrypt setup`

- Enable filesystem encryption for a directory:

`fscrypt encrypt /path/to/dir`

- Unlock an encrypted directory:

`fscrypt unlock /path/to/dir`

- Lock an encrypted directory:

`fscrypt lock /path/to/dir`
