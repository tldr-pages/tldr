# parted

> A partition manipulation program.
> See also: `parted-interactive`, `partprobe`.
> More information: <https://www.gnu.org/software/parted/parted.html>.

- List partitions on all block devices:

`sudo parted --list`

- Create a new partition table of the specified label-type:

`sudo parted {{/dev/sdX}} --script mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Create a new `gpt` partition table with a 500MiB boot partition and give the rest for the system partition:

`sudo parted {{/dev/sdX}} --script mklabel gpt mkpart primary 0% 500MiB mkpart primary 500MiB 100%`

- Start interactive mode with the specified disk selected:

`sudo parted {{/dev/sdX}}`
