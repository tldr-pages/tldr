# qemu-img

> Create and manipulate Quick Emulator Virtual HDD images.
> More information: <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>.

- Create disk image with a specific size (in gigabytes):

`qemu-img create {{path/to/image_file.img}} {{gigabytes}}G`

- Show information about a disk image:

`qemu-img info {{path/to/image_file.img}}`

- Increase or decrease image size:

`qemu-img resize {{path/to/image_file.img}} {{gigabytes}}G`

- Dump the allocation state of every sector of the specified disk image:

`qemu-img map {{path/to/image_file.img}}`

- Convert a VMware .vmdk disk image to a KVM .qcow2 disk image:

`qemu-img convert -f {{vmdk}} -O {{qcow2}} {{path/to/image_file.vmdk}} {{path/to/image_file.qcow2}}`

- Create an internal snapshot of a KVM .qcow2 disk image:

`qemu-img snapshot -c {{snapshot_tag_name}} {{path/to/image_file.qcow2}}`

- Apply an internal snapshot to a KVM .qcow2 disk image:

`qemu-img snapshot -a {{snapshot_tag_name}} {{path/to/image_file.qcow2}}`
