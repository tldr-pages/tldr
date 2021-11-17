# btrfs restore

> Try to salvage files from a damaged btrfs filesystem
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-restore>.

- Restore all files from btrfs filesystem to given directory:

`sudo btrfs restore {{path/to/btrfs-device}} {{path/to/target-directory}}`

- List (don't write) files to be restored from btrfs filesystem:

`sudo btrfs restore --dry-run {{path/to/btrfs-device}} {{path/to/target-directory}}`

- Restore files matching regex (`c`ase-insensitive) files to be restored from btrfs filesystem (all parent directories of target file(s) must match as well):

`sudo btrfs restore --path-regex {{regex}} -c {{path/to/btrfs-device}} {{path/to/target-directory}}`

- Restore files from btrfs filesystem using specific root tree `bytenr` (see `btrfs-find-root`)

`sudo btrfs restore -t {{bytenr}} {{path/to/btrfs-device}} {{path/to/target-directory}}`

- Restore files from a btrfs filesystem (along with `m`etadata, e`x`tended attributes, and `S`ymlinks), `o`verwriting files in target:

`sudo btrfs restore -m -x -S -o {{path/to/btrfs-device}} {{path/to/target-directory}}`
