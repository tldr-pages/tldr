# kernel-install

> Add and remove kernel and initrd images to and from `/boot`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/kernel-install.html>.

- Show the current kernel configuration that have been configured or auto-detected:

`kernel-install`

- Show configuration for a specific kernel:

`kernel-install inspect {{path/to/kernel-image}}`

- Add a kernel to bootloader partition:

`sudo kernel-install add {{kernel-version}} {{path/to/kernel-image}}`

- Add kernel and initramfs images to bootloader partition:

`sudo kernel-install add {{kernel-version}} {{path/to/kernel-image}} {{path/to/initrd-file ...}}`

- Remove kernel from the bootloader partition:

`sudo kernel-install remove {{kernel-version}}`
