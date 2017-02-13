# vgcreate

> Create a volume group.

- Creates a new volume group called vol_grp_name using /dev/sda1

`vgcreate {{vol_grp_name}} {{/dev/sda1}}`

- Creates a new volume group called vol_grp_name using multiple devices

`vgcreate {{vol_grp_name}} {{/dev/sda1}} {{/dev/sdb1}} {{/dev/sdc1}}`
