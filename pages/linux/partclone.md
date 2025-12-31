# partclone

> Copy and restore partitions to and from an image while disregarding empty blocks.
> More information: <https://manned.org/partclone>.

- Copy a partition into an image:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{/dev/sdXY}} {{[-o|--output]}} {{path/to/backup.img}}`

- Restore a partition from an image:

`sudo partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-c|--clone]}} {{[-s|--source]}} {{path/to/backup.img}} {{[-o|--output]}} {{/dev/sdXY}}`

- Display help:

`partclone.{{ext4|btrfs|fat32|xfs|...}} {{[-h|--help]}}`
