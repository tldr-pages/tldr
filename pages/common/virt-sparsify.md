# virt-sparsify

> libguestfs tool to to make a virtual machine drive images thin-provisioned.
> Use only for offline machines to avoid data corruption.

- Create sparsified comporessed image without snapshots from unsparsified:

`virt-sparsify --compress {{image.qcow2}} {{image_new.qcow2}}`

- Sparsify image in place:

`virt-sparsify --in-place {{/var/lib/libvirt/images/image.img}}`
