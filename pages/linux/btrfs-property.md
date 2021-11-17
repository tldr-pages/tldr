# btrfs property

> Get/Set/List properties for given btrfs filesystem object (file/directory/subvolume/filesystem/device).
> More information: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-property>.

- List available properties (+description) for the given btrfs object (file/directory/subvolume/filesystem/device):

`sudo btrfs property list {{path/to/btrfs_object}}`

- Get all properties for the given btrfs object:

`sudo btrfs property get {{path/to/btrfs_object}}`

- Get `label` property for the given btrfs filesystem/device:

`sudo btrfs property get {{path/to/btrfs_filesystem}} label`

- Get all object-type specific properties for the given btrfs filesystem/device:

`sudo btrfs property get -t {{subvol|filesystem|inode|device}} {{path/to/btrfs_filesystem}}`

- Set `compression` property for the given btrfs inode (file/directory):

`sudo btrfs property set {{path/to/btrfs_inode}} compression {{zstd|zlib|lzo|none}}`
