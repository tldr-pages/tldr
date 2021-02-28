# lvresize

> Change the size of a logical volume.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/index>.

- Change the size of a logical volume to 120GB:

`lvresize --size {{120G}} {{volume_group}}/{{logical_volume}}`

- Extend the size of a logical volume as well as the underlying filesystem by 120GB:

`lvresize --size +{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

- Extend the size of a logical volume to 100% of the free physical volume space:

`lvresize --size {{100}}%FREE {{volume_group}}/{{logical_volume}}`

- Reduce the size of a logical volume as well as the underlying filesystem by 120GB:

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`
