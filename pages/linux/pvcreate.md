# pvcreate

> Initialize a disk or partition for use as a physical volume.
> See also: `lvm`.
> More information: <https://manned.org/pvcreate>.

- Initialize the `/dev/sda1` volume for use by LVM:

`pvcreate {{/dev/sdXY}}`

- Force the creation without any confirmation prompts:

`pvcreate {{[-f|--force]}} {{/dev/sdXY}}`
