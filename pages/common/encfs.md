# encfs

> Encrypted virtual filesystem.
> More information: <https://github.com/vgough/encfs>.

- Initialize or mount an encrypted filesystem:

`encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Initialize an encrypted filesystem with standard settings:

`encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Run encfs in foreground instead of spawning a daemon:

`encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Unmount an encrypted filesystem:

`fusermount -u {{/path/to/mount_point}}`

- Mount an encrypted snapshot of a plain directory:

`encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
