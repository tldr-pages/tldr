# pvcreate

> Initialize a disk or partition for use by LVM.

- Initialize /dev/sda1 to use lvm:

`pvcreate {{/dev/sda1}}`

- Force the creation without any confirmation:

`pvcreate --force {{/dev/sda1}}`
