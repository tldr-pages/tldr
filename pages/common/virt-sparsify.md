# virt-sparsify

> libguestfs tool to to make a virtual machine drive images thin-provisioned.
> Use only for offline machines to avoid data corruption.
> Home page: <https://libguestfs.org/>.

- Create a sparsified compressed image without snapshots from an unsparsified one:

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/image_new.qcow2}}`

- Sparsify an image in-place:

`virt-sparsify --in-place {{/var/lib/libvirt/images/image.img}}`
