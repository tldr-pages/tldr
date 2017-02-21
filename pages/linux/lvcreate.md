# lvcreate

> Creates a logical volume in an existing volume group.

- Create a logical volume 10 gigabytes in size in the volume group vg1:

`lvcreate -L {{10G}} {{vg1}}`

- Create a 1500 megabyte linear logical volume named mylv in the volume group vg1:

`lvcreate -L {{1500}} -n {{mylv}} {{vg1}}`

- Create a logical volume called mylv that uses 60% of the total space in volume group vg1:

`lvcreate -l {{60%VG}} -n {{mylv}} {{vg1}}`

- Create a logical volume called mylv that uses all of the unallocated space in the volume group vg1:

`lvcreate -l {{100%FREE}} -n {{mylv}} {{vg1}}`
