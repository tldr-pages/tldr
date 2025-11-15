# qemu-system-x86_64

> Emulate the `x86_64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Boot from an image emulating the `x86_64` architecture:

`qemu-system-x86_64 -hda {{image_name.img}} -m {{4096}}`

- Boot a QEMU instance from a live ISO image:

`qemu-system-x86_64 -hda {{image_name.img}} -m {{4096}} -cdrom {{os_image.iso}} -boot d`

- Boot from a physical device (e.g. from USB to test a bootable medium):

`qemu-system-x86_64 -hda {{/dev/storage_device}} -m {{4096}}`

- Do not launch a VNC server:

`qemu-system-x86_64 -hda {{image_name.img}} -m {{4096}} -nographic`

- Exit non-graphical QEMU:

`<Ctrl a><x>`

- List the supported machine types:

`qemu-system-x86_64 {{[-M|-machine]}} help`
