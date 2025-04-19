# eclean-kernel

> Remove old kernels in Gentoo.
> More information: <https://wiki.gentoo.org/wiki/Kernel/Removal#Using_eclean-kernel>.

- List all kernel files:

`sudo eclean-kernel -l`

- Remove all kernels, but leave the newest two kernels:

`sudo eclean-kernel -n 2`

- Remove all kernels, but leave the [n]ewest two kernels and [a]sk before removal:

`sudo eclean-kernel -a -n 2`
