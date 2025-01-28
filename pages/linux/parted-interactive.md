# parted

> A partition manipulation program.
> See also: `partprobe`.
> More information: <https://www.gnu.org/software/parted/parted.html>.

- Start interactive mode with the specified disk selected:

`sudo parted {{/dev/sdX}}`

- Show partition information in interactive mode:

`print`

- Select a disk in interactive mode:

`select {{/dev/sdX}}`

- Create a 16 GB partition with the specified filesystem in interactive mode:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- Resize a partition in interactive mode:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Remove a partition in interactive mode:

`rm {{/dev/sdXN}}`
