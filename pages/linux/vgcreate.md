# vgcreate

> Create a volume group.

- Create a new volume group called vg1 using `/dev/sda1`:

`vgcreate {{vg1}} {{/dev/sda1}}`

- Create a new volume group called vg1 using multiple devices:

`vgcreate {{vg1}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
