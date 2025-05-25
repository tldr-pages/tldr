# parted

> A partition manipulation program.
> See also: `parted-interactive`, `partprobe`.
> More information: <https://www.gnu.org/software/parted/manual/html_node/Invoking-Parted.html>.

- List partitions on all block devices:

`sudo parted {{[-l|--list]}}`

- Create a new partition table of the specified label-type:

`sudo parted {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Create a new `gpt` partition table with a 500MiB boot partition and give the rest for the system partition (`--script` skips user intervention prompts):

`sudo parted {{/dev/sdX}} {{[-s|--script]}} mklabel gpt mkpart "{{boot_partition_name}}" 0% 500MiB mkpart "{{system_partition_name}}" 500MiB 100%`

- Set a partition to have its boot flag turned on:

`sudo parted {{/dev/sdX}} set {{1}} boot on`

- Start interactive mode with the specified disk selected:

`sudo parted {{/dev/sdX}}`

- Display help:

`parted {{[-h|--help]}}`
