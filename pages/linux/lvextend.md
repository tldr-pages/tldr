# lvextend

> Increase the size of a logical volume.
> See also: `lvm`.
> More information: <https://manned.org/lvextend>.

- Increase a volume's size to 120 GB:

`sudo lvextend {{[-L|--size]}} {{120G}} {{logical_volume}}`

- Increase a volume's size by 40 GB as well as the underlying filesystem:

`sudo lvextend {{[-L|--size]}} +{{40G}} {{[-r|--resizefs]}} {{logical_volume}}`

- Increase a volume's size to 100% of the free physical volume space:

`sudo lvextend {{[-l|--extents]}} +{{100}}%FREE {{logical_volume}}`

- Increase a volume's size to 100% of the free physical volume space and resize the underlying filesystem:

`sudo lvextend {{[-l|--extents]}} +{{100}}%FREE {{[-r|--resizefs]}} {{logical_volume}}`
