# btrfs restore

> Try to salvage files from a damaged btrfs filesystem.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs-restore.html>.

- Restore all files from a btrfs filesystem to a given directory:

`sudo btrfs {{[rest|restore]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- List (don't write) files to be restored from a btrfs filesystem:

`sudo btrfs {{[rest|restore]}} {{[-D|--dry-run]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files matching a given `regex` ([c]ase-insensitive) files to be restored from a btrfs filesystem (all parent directories of target file(s) must match as well):

`sudo btrfs {{[rest|restore]}} --path-regex {{regex}} -c {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files from a btrfs filesystem using a specific root [t]ree `bytenr` (see `btrfs-find-root`):

`sudo btrfs {{[rest|restore]}} -t {{bytenr}} {{path/to/btrfs_device}} {{path/to/target_directory}}`

- Restore files from a btrfs filesystem (along with metadata, extended attributes, and Symlinks), overwriting files in the target:

`sudo btrfs {{[rest|restore]}} {{[-m|--metadata]}} {{[-x|--xattr]}} {{[-S|--symlinks]}} {{[-o|--overwrite]}} {{path/to/btrfs_device}} {{path/to/target_directory}}`
