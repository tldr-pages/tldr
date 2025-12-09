# eselect kernel

> An `eselect` module for managing the `/usr/src/linux` symlink.
> More information: <https://wiki.gentoo.org/wiki/Eselect#Kernel>.

- List available kernel symlink targets with their numbers:

`eselect kernel list`

- Set the `/usr/src/linux` symlink by name or number from the `list` command:

`eselect kernel set {{name|number}}`

- Show what the current kernel symlink points to:

`eselect kernel show`

- Set the kernel symlink to the currently running kernel:

`eselect kernel update`
