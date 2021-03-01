# lvcreate

> Creates a logical volume in an existing volume group. A volume group is a collection of logical and physical volumes.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes>.

- Create a logical volume of 10 gigabytes in the volume group vg1:

`lvcreate -L {{10G}} {{vg1}}`

- Create a 1500 megabyte linear logical volume named mylv in the volume group vg1:

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- Create a logical volume called mylv that uses 60% of the total space in volume group vg1:

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- Create a logical volume called mylv that uses all of the unallocated space in the volume group vg1:

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`
