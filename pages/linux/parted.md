# parted

> A partition manipulation program.
> More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`parted --list`

- Start to manipulate disk partition:

`parted {{/dev/sdX}}`

- Create a new partition table of label-type directly, label-type can be gpt, msdos etc:

`parted --script {{/dev/sdX}} {{mklabel gpt}}`

- Show disk partition information in interactive mode:

`print`

- Select a disk in interactive mode:

`select {{/dev/sdX}}`

- Create a 16GB primary partition with ext4 file type in interactive mode:

`mkpart {{primary}} {{ext4}} {{1}} {{16G}}`

- Resize partition size:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Remove partition:

`rm {{/dev/sdXN}}`
