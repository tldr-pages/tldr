# mkinitcpio

> Bash script for create an initial ramdisk environment.
> More information: <https://man.archlinux.org/man/mkinitcpio.8>.

- Do a dry run and display the output:

`mkinitcpio`

- Generate the preset provided by `linux` package:

`mkinitcpio --preset {{linux}}`

- Generate the preset provided by `linux-lts` package:

`mkinitcpio --preset {{linux-lts}}`

- Generate all existing presets (used to regenerate all the initramfs images after a change in `/etc/mkinitcpio.conf`):

`mkinitcpio --allpresets`

- Generate an image using an alternative configuration file:

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- Generate an image for a kernel other than the one currently running (the installed kernel releases can be found in `/usr/lib/modules/`):

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- List all available hooks:

`mkinitcpio --listhooks`

- Display help for a specific hook:

`mkinitcpio --hookhelp {{hook_name}}`
