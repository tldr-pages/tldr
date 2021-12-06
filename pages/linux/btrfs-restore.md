# btrfs restore

> Try to salvage files from a damaged btrfs filesystem.
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-restore>.

- Restore all files from btrfs filesystem to given directory:

`sudo btrfs restore {{path/to/btrfs_device}} {{path/to/target_directory}}`

- List (don't write) files to be restored from btrfs filesystem:

`sudo btrfs restore --dry-run {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files matching regex ([c]ase-insensitive) files to be restored from btrfs filesystem (all parent directories of target file(s) must match as well):

`sudo btrfs restore --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files from btrfs filesystem using specific root tree `bytenr` (see `btrfs-find-root`):

`sudo btrfs restore -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files from a btrfs filesystem (along with metadata, extended attributes, and Symlinks), overwriting files in target:

`sudo btrfs restore --metadata --xattr --symlinks --overwrite {{path/to/btrfs_device}} {{path/to/target_directory}}`
