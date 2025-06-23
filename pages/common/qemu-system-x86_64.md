# qemu-system-x86_64

> Emulate `x86_64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Boot from image emulating x64 architecture:

`qemu-system-x86_64 -hda {{image_name.img}}`

- Boot QEMU instance with a live ISO image:

`qemu-system-x86_64 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d`

- Specify amount of RAM for instance:

`qemu-system-x86_64 -m 256 -hda {{image_name.img}} -cdrom {{os-image.iso}} -boot d`

- Boot from physical device (e.g. from USB to test bootable medium):

`qemu-system-x86_64 -hda {{/dev/storage_device}}`
