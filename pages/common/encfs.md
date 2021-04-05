# encfs

> Mounts or creates encrypted virtual filesystems.
> See also `fusermount`, which can unmount filesystems mounted by this command.
> More information: <https://github.com/vgough/encfs>.

- Initialize or mount an encrypted filesystem:

`encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Initialize an encrypted filesystem with standard settings:

`encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Run encfs in the foreground instead of spawning a daemon:

`encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Mount an encrypted snapshot of a plain directory:

`encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
