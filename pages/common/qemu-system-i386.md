# qemu-system-i386

> Emulate the `i386` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Boot from an image emulating the `i386` architecture:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}}`

- Boot a QEMU instance from a live ISO image:

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d -m {{4096}}`

- Boot from a physical device (e.g. from USB to test a bootable medium):

`qemu-system-i386 -hda {{/dev/storage_device}} -m {{4096}}`

- Do not launch a VNC server:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}} -nographic`

- Exit non-graphical QEMU:

`<Ctrl a><x>`

- List the supported machine types:

`qemu-system-x86_64 {{[-M|-machine]}} help`
