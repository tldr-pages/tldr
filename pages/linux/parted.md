# parted

> A partition manipulation program.
> See also: `partprobe`.
> More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`sudo parted --list`

- Start interactive mode with the specified disk selected:

`sudo parted {{/dev/sdX}}`

- Create a new partition table of the specified label-type:

`sudo parted {{/dev/sdX}} --script mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Create a new `gpt` partition table with a 500MiB boot partition and set the rest for system:

`sudo parted {{/dev/sdX}} --script mklabel gpt mkpart primary 0% 500MiB mkpart primary 500MiB 100%`

- Show partition information in interactive mode:

`print`

- Create a 16 GB partition with the specified filesystem in interactive mode:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- Resize a partition in interactive mode:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Remove a partition in interactive mode:

`rm {{/dev/sdXN}}`
