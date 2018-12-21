# pvcreate

> Initialize a physical volume (disk or partition) for use by the Logical Volume Manager (LVM).

- Initialize the `/dev/sda1` volume for use by LVM:

`pvcreate {{/dev/sda1}}`

- Force the creation without any confirmation prompts:

`pvcreate --force {{/dev/sda1}}`
