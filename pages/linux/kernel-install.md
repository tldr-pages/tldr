# kernel-install

> Add and remove kernel and initrd images to and from `/boot`.
> More information: <https://manned.org/kernel-install.8>.

- Add kernel and initramfs images to bootloader partition:

`sudo kernel-install add {{kernel-version}} {{kernel-image}} {{path/to/initrd-file ...}}`

- Remove kernel from the bootloader partition:

`sudo kernel-install remove {{kernel-version}}`

- Show various paths and parameters that have been configured or auto-detected:

`sudo kernel-install inspect {{kernel-image}}`
