# btrfs

> A filesystem based on the copy-on-write (COW) principle for Linux.
> Some subcommands such as `device` have their own usage documentation.
> More information: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Create subvolume:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{path/to/subvolume}}`

- List subvolumes:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{path/to/mount_point}}`

- Show space usage information:

`sudo btrfs {{[f|filesystem]}} df {{path/to/mount_point}}`

- Enable quota:

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{path/to/subvolume}}`

- Show quota:

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{path/to/subvolume}}`
