# lvcreate

> Create a logical volume in an existing volume group. A volume group is a collection of logical and physical volumes.
> See also: `lvm`.
> More information: <https://manned.org/lvcreate>.

- Create a logical volume of 10 gigabytes in the volume group `vg1`:

`sudo lvcreate {{[-L|--size]}} 10G vg1`

- Create a 1500 megabyte linear logical volume named `mylv` in the volume group `vg1`:

`sudo lvcreate {{[-L|--size]}} 1500 {{[-n|--name]}} mylv vg1`

- Create a logical volume called `mylv` that uses 60% of the total space in volume group `vg1`:

`sudo lvcreate {{[-l|--extents]}} 60%VG {{[-n|--name]}} mylv vg1`

- Create a logical volume called `mylv` that uses all the unallocated space in the volume group `vg1`:

`sudo lvcreate {{[-l|--extents]}} 100%FREE {{[-n|--name]}} mylv vg1`
