# qemu-system-x86_64

> Emulate `x86_64` architecture.
> More information: <https://www.qemu.org/docs/master/system/target-i386.html>.

- Boot from image emulating x64 architecture:

`qemu-system-x86_64 -hda {{image_name.img}} -m {{4096}}`

- Boot QEMU instance with a live ISO image:

`qemu-system-x86_64 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d -m {{4096}}`

- Boot from physical device (e.g. from USB to test bootable medium):

`qemu-system-x86_64 -hda {{/dev/storage_device}} -m {{4096}}`

- Do not launch a VNC server:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}} -nographic`

- Exit non-graphical QEMU:

`<Ctrl a><x>`
