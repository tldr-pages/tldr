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

- Create a 16GB part-type partition for filesystem type in interactive mode, (part-type should be one of "primary", "logical", or "extended"):

`mkpart {{part-type}} {{filesystem-type}} {{0%}} {{16G}}`

- Resize partition size:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Remove partition:

`rm {{/dev/sdXN}}`
