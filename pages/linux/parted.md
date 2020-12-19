# parted

> A partition manipulation program.
> More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`sudo parted --list`

- Start to manipulate disk partition:

`sudo parted {{/dev/sdX}}`

- Create a new partition table of label-type directly, label-type can be gpt, msdos etc:

`sudo parted --script {{/dev/sdX}} mklabel {{gpt}}`

- Show disk partition information in interactive mode:

`print`

- Select a disk in interactive mode:

`select {{/dev/sdX}}`

- Interactively create a 16GB partition with a given filesystem:

`mkpart {{primary|logical|extended}} {{filesystem}} {{0%}} {{16G}}`

- Resize partition size:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Remove partition:

`rm {{/dev/sdXN}}`
