# mkinitcpio

> Generate initial ramdisk environments for booting the Linux kernel based on the specified preset(s).
> More information: <https://manned.org/mkinitcpio>.

- Perform a dry run (print what would be done without actually doing it):

`mkinitcpio`

- Generate ramdisk environments based on all existing presets (used to regenerate all the initramfs images after a change in `/etc/mkinitcpio.conf`):

`sudo mkinitcpio {{[-P|--allpresets]}}`

- Generate a ramdisk environment based on the `linux` preset:

`sudo mkinitcpio {{[-p|--preset]}} linux`

- Generate a ramdisk environment based on the `linux-lts` preset:

`sudo mkinitcpio {{[-p|--preset]}} linux-lts`

- Generate an initramfs image using an alternative configuration file:

`sudo mkinitcpio {{[-c|--config]}} {{path/to/mkinitcpio.conf}} {{[-g|--generate]}} {{path/to/initramfs.img}}`

- Generate an initramfs image for a kernel other than the one currently running (the installed kernel releases can be found in `/usr/lib/modules/`):

`sudo mkinitcpio {{[-k|--kernel]}} {{kernel_version}} {{[-g|--generate]}} {{path/to/initramfs.img}}`

- List all available hooks:

`mkinitcpio {{[-L|--listhooks]}}`

- Display help for a specific hook:

`mkinitcpio {{[-H|--hookhelp]}} {{hook_name}}`
