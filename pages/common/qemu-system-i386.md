# qemu-system-i386

> Emulate `i386` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Boot from image emulating i386 architecture:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}}`

- Boot QEMU instance with a live ISO image:

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d -m {{4096}}`

- Boot from physical device (e.g. from USB to test bootable medium):

`qemu-system-i386 -hda {{/dev/storage_device}} -m {{4096}}`
