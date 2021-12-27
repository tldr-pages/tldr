# btrfs property

> Get, set, or list properties for a given btrfs filesystem object (files, directories, subvolumes, filesystems, or devices).
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-property>.

- List available properties (and descriptions) for the given btrfs object:

`sudo btrfs property list {{path/to/btrfs_object}}`

- Get all properties for the given btrfs object:

`sudo btrfs property get {{path/to/btrfs_object}}`

- Get the `label` property for the given btrfs filesystem or device:

`sudo btrfs property get {{path/to/btrfs_filesystem}} label`

- Get all object type-specific properties for the given btrfs filesystem or device:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{path/to/btrfs_filesystem}}`

- Set the `compression` property for a given btrfs inode (either a file or directory):

`sudo btrfs property set {{path/to/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`
