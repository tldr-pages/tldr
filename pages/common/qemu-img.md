# qemu-img

> Tool for QEMU Virtual HDD image creation and manipulation.

- Create disk image with a specific size (in gigabytes):

`qemu-img create {{image_name.img}} {{gigabites}}G`

- Get information about image:

`qemu-img info {{image_name.img}}`

- Increase/decrease image size:

`qemu-img resize {{image_name.img}} {{gigabites}}G`

- Dump the allocation state of every sector of the specified disk image:

`qemu-img map {{image_name.img}}`
