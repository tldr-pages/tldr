# dracut

> Generate initramfs images to boot the Linux kernel.
> Dracut uses options from configuration files in `/etc/dracut.conf`, `/etc/dracut.conf.d/*.conf` and `/usr/lib/dracut/dracut.conf.d/*.conf` by default.
> More information: <https://github.com/dracutdevs/dracut/wiki>.

- Generate an initramfs image for the current kernel without overriding any options:

`dracut`

- Generate an initramfs image for the current kernel and overwrite the existing one:

`dracut --force`

- Generate an initramfs image for a specific kernel:

`dracut --kver {{kernel_version}}`

- Show a list of available modules:

`dracut --list-modules`
