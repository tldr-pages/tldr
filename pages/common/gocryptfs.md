# gocryptfs

> Encrypted overlay filesystem written in Go.
> More information: <https://github.com/rfjakob/gocryptfs#use>.

- Initialize an encrypted filesystem:

`gocryptfs -init {{path/to/cipher_directory}}`

- Mount an encrypted filesystem:

`gocryptfs {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Mount with the explicit master key instead of password:

`gocryptfs --masterkey {{path/to/cipher_directory}} {{path/to/mount_point}}`

- Change the password:

`gocryptfs --passwd {{path/to/cipher_directory}}`

- Make an encrypted snapshot of a plain directory:

`gocryptfs --reverse {{path/to/plain_directory}} {{path/to/cipher_directory}}`
