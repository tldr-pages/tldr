# cryfs

> A cryptographic filesystem for the cloud.
> More information: <https://www.cryfs.org/>.

- Mount an encrypted filesystem. The initialization wizard will be started on the first execution:

`cryfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Unmount an encrypted filesystem:

`cryfs-unmount {{path/to/mount_point}}`

- Automatically unmount after ten minutes of inactivity:

`cryfs --unmount-idle {{10}} {{path/to/cipher_dir}} {{path/to/mount_point}}`

- List supported ciphers:

`cryfs --show-ciphers`
