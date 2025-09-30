# mkfs.bcachefs

> Create a `bcachefs` filesystem inside a partition.
> See also: `bcachefs`.
> More information: <https://bcachefs-docs.readthedocs.io/en/latest/mgmt-formatting.html>.

- Create a `bcachefs` filesystem inside partition `Y` on a device `X`:

`sudo mkfs.bcachefs {{/dev/sdXY}}`

- Create a `bcachefs` filesystem with a volume label:

`sudo mkfs.bcachefs {{[-L|--fs_label]}} {{volume_label}} {{/dev/sdXY}}`
