# virt-sparsify

> Make virtual machine drive images thin-provisioned.
> Note: Use only for offline machines to avoid data corruption.
> More information: <https://manned.org/virt-sparsify>.

- Create a sparsified compressed image without snapshots from an unsparsified one:

`virt-sparsify --compress {{path/to/image.qcow2}} {{path/to/new_image.qcow2}}`

- Sparsify an image in-place:

`virt-sparsify --in-place {{path/to/image.img}}`

- Convert from one image format to another:

`virt-sparsify {{path/to/image}} --convert {{qcow2|raw|vdi|...}} {{path/to/new_image}}`
