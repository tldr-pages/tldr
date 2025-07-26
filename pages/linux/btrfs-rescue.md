# btrfs rescue

> Try to recover a damaged btrfs filesystem.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Rebuild the filesystem metadata tree (very slow):

`sudo btrfs {{[resc|rescue]}} {{[ch|chunk-recover]}} {{path/to/partition}}`

- Fix device size alignment related problems (e.g. unable to mount the filesystem with super total bytes mismatch):

`sudo btrfs {{[resc|rescue]}} {{[fix-de|fix-device-size]}} {{path/to/partition}}`

- Recover a corrupted superblock from correct copies (recover the root of filesystem tree):

`sudo btrfs {{[resc|rescue]}} {{[s|super-recover]}} {{path/to/partition}}`

- Recover from an interrupted transactions (fixes log replay problems):

`sudo btrfs {{[resc|rescue]}} {{[z|zero-log]}} {{path/to/partition}}`

- Create a `/dev/btrfs-control` control device when `mknod` is not installed:

`sudo btrfs {{[resc|rescue]}} {{[c|create-control-device]}}`
