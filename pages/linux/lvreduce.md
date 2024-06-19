# lvreduce

> Reduce the size of a logical volume.
> See also: `lvm`.
> More information: <https://manned.org/lvreduce>.

- Reduce a volume's size to 120 GB:

`lvreduce --size {{120G}} {{logical_volume}}`

- Reduce a volume's size by 40 GB as well as the underlying filesystem:

`lvreduce --size -{{40G}} -r {{logical_volume}}`
