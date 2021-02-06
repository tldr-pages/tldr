# arch-chroot

> Enhanced `chroot` command for Arch Linux installation.
> More information: <https://man.archlinux.org/man/arch-chroot.8>.

- Start interactive shell in a new root directory:

`arch-chroot {{path/to/new/root}}`

- Specify user to run as:

`arch-chroot -u {{user}} {{path/to/new/root}}`

- Run a command in a new root directory:

`arch-chroot {{path/to/new/root}} {{command}} {{command_arguments}}`

- Generate the initial ramdisk using the preset provided by the `linux` package on new root directory:

`arch-chroot {{path/to/new/root}} {{mkinitcpio --preset linux}}`

- Start a zsh session in a new root directory (the `zsh` package should be installed in the target):

`arch-chroot {{path/to/new/root}} {{zsh}}`
