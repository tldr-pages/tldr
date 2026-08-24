# fscrypt

> Go tool for managing Linux filesystem encryption.
> More information: <https://github.com/google/fscrypt#example-usage>.

- Prepare the root filesystem for use with `fscrypt`:

`sudo fscrypt setup`

- Prepare a specific mountpoint for use with `fscrypt`:

`fscrypt setup {{path/to/directory}}`

- Enable filesystem encryption for a directory:

`fscrypt encrypt {{path/to/directory}}`

- Unlock an encrypted directory:

`fscrypt unlock {{path/to/encrypted_directory}}`

- Lock an encrypted directory:

`fscrypt lock {{path/to/encrypted_directory}}`
