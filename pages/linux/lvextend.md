# lvextend

> Increase the size of a logical volume.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/logical_volume_manager_administration>.

- Increase a volume's size to 120GB:

`lvextend --size {{120G}} {{logical_volume}}`

- Increase a volume's size by 40GB as well as the underlying filesystem:

`lvextend --size +{{40G}} -r {{logical_volume}}`

- Increase a volume's size to 100% of the free physical volume space:

`lvextend --size {{100}}%FREE {{logical_volume}}`
