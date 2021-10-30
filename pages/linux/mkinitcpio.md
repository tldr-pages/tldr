# mkinitcpio

> Generates initial ramdisk environments for booting the Linux kernel based on the specified preset(s).
> More information: <https://man.archlinux.org/man/mkinitcpio.8>.

- Perform a dry run (print what would be done without actually doing it):

`mkinitcpio`

- Generate a ramdisk environment based on the `linux` preset:

`mkinitcpio --preset {{linux}}`

- Generate a ramdisk environment based on the `linux-lts` preset:

`mkinitcpio --preset {{linux-lts}}`

- Generate ramdisk environments based on all existing presets (used to regenerate all the initramfs images after a change in `/etc/mkinitcpio.conf`):

`mkinitcpio --allpresets`

- Generate an initramfs image using an alternative configuration file:

`mkinitcpio --config {{path/to/mkinitcpio.conf}} --generate {{path/to/initramfs.img}}`

- Generate an initramfs image for a kernel other than the one currently running (the installed kernel releases can be found in `/usr/lib/modules/`):

`mkinitcpio --kernel {{kernel_version}} --generate {{path/to/initramfs.img}}`

- List all available hooks:

`mkinitcpio --listhooks`

- Display help for a specific hook:

`mkinitcpio --hookhelp {{hook_name}}`
