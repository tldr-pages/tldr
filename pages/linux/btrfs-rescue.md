# btrfs rescue

> Try to recover a damaged btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-rescue>.

- To rebuild filesystem metadata tree (very slow):

`sudo btrfs rescue chunk-recover {{path/to/btrfs_mount}}`

- To fix device size alignment related problems (like unable to mount the fs with super total bytes mismatch)

`sudo btrfs rescue fix-device-size {{path/to/btrfs_mount}}`

- To recover corrupted superblock from correct copies (recover the root of filesystem tree)

`sudo btrfs rescue super-recover {{path/to/btrfs_mount}}`

- To recover from interrupted transactions (fixes log replay problems):

`sudo btrfs rescue zero-log {{path/to/btrfs_mount}}`

- To create a /dev/btrfs-control control device when mknod is not installed:

`sudo btrfs rescue create-control-device`
