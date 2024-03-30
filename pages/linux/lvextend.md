# lvextend

> Increase the size of a logical volume.
> See also: `lvm`.
> More information: <https://manned.org/lvextend.8>.

- Increase a volume's size to 120 GB:

`lvextend --size {{120G}} {{logical_volume}}`

- Increase a volume's size by 40 GB as well as the underlying filesystem:

`lvextend --size +{{40G}} -r {{logical_volume}}`

- Increase a volume's size to 100% of the free physical volume space:

`lvextend --size +{{100}}%FREE {{logical_volume}}`
