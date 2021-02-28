# lvreduce

> Reduce the size of a logical volume.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/logical_volume_manager_administration>.

- Reduce a volume's size to 120GB:

`lvreduce --size {{120G}} {{logical_volume}}`

- Reduce a volume's size by 40GB as well as the underlying filesystem:

`lvreduce --size -{{40G}} -r {{logical_volume}}`
