# lvresize

> Change the size of a logical volume.
> More information: https://man7.org/linux/man-pages/man8/lvresize.8.html.

- Change a logical volume's size to 120GB:

`lvresize --size {{120G}} {{volume_group}}/{{logical_volume}}`

- Extend a logical volume's size by 120GB as well as the underlying filesystem:

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`

- Extend a logical volume's size to 100% of the free physical volume space:

`lvresize --size {{100}}%FREE {{volume_group}}/{{logical_volume}}`

- Reduce a logical volume's size by 120GB as well as the underlying filesystem:

`lvresize --size -{{120G}} --resizefs {{volume_group}}/{{logical_volume}}`
