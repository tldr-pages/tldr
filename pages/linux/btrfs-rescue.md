# btrfs rescue

> Try to recover a damaged btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- Rebuild the filesystem metadata tree (very slow):

`sudo btrfs rescue chunk-recover {{path/to/partition}}`

- Fix device size alignment related problems (e.g. unable to mount the filesystem with super total bytes mismatch):

`sudo btrfs rescue fix-device-size {{path/to/partition}}`

- Recover a corrupted superblock from correct copies (recover the root of filesystem tree):

`sudo btrfs rescue super-recover {{path/to/partition}}`

- Recover from an interrupted transactions (fixes log replay problems):

`sudo btrfs rescue zero-log {{path/to/partition}}`

- Create a `/dev/btrfs-control` control device when `mknod` is not installed:

`sudo btrfs rescue create-control-device`
