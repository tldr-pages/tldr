# pvcreate

> Initialize a disk or partition for use as a physical volume.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/logical_volume_manager_administration>.

- Initialize the `/dev/sda1` volume for use by LVM:

`pvcreate {{/dev/sda1}}`

- Force the creation without any confirmation prompts:

`pvcreate --force {{/dev/sda1}}`
