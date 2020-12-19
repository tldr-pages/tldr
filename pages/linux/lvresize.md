# lvresize

> Change the size of a logical volume.

- Change a volume's size to 120GB:

`lvresize -L {{120G}} {{logical_volume}}`

- Reduce a volume's size by 120GB as well as the underlying filesystem:

`lvresize --size -{{120G}} -r {{logical_volume}}`

- Increase a volume's size to 100% of the free physical volume space:

`lvresize --size {{100}}%FREE {{logical_volume}}`
