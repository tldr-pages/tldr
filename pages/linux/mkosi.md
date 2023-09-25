# mkosi

> Tool for building modern, legacy-free Linux images.
> Part of `systemd`.
> More information: <https://manned.org/mkosi>.

- Show current build configuration to verify what would be built:

`mkosi summary`

- Build an image with default settings, if no distribution is selected, distribution of the host system is used:

`mkosi build --distribution={{fedora|debian|ubuntu|arch|opensuse}}`

- Build image and get interactive shell in a systemd-nspawn container of the image:

`mkosi shell`

- Boot image in a virtual machine using QEMU, only supported for disk images or CPIO images when a kernel is provided:

`mkosi qemu`

- Display help:

`mkosi help`
