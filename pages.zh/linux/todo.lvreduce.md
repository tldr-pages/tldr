# lvreduce

> Reduce the size of a logical volume.

- Reduce a volume's size to 120GB:

`lvreduce --size {{120G}} {{logical_volume}}`

- Reduce a volume's size by 40GB as well as the underlying filesystem:

`lvreduce --size -{{40G}} -r {{logical_volume}}`
