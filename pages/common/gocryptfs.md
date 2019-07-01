# gocryptfs

> Encrypted overlay filesystem written in Go.
> More information: <https://github.com/rfjakob/gocryptfs>.

- Initialize an encrypted filesystem:

`gocryptfs -init {{path/to/cipher_dir}}`

- Mount an encrypted filesystem:

`gocryptfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Mount with the explicit master key instead of password:

`gocryptfs --masterkey {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Change the password:

`gocryptfs --passwd {{path/to/cipher_dir}}`

- Make an encrypted snapshot of a plain directory:

`gocryptfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
