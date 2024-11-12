# mkfs.bcachefs

> Create a `bcachefs` filesystem inside a partition.
> More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- Create a `bcachefs` filesystem inside partition 1 on a device (`X`):

`sudo mkfs.bcachefs {{/dev/sdX1}}`

- Create a `bcachefs` filesystem with a volume label:

`sudo mkfs.bcachefs {{-L|--fs_label}} {{volume_label}} {{/dev/sdX1}}`
