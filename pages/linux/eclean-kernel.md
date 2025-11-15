# eclean-kernel

> Remove old kernels in Gentoo.
> More information: <https://wiki.gentoo.org/wiki/Kernel/Removal#Using_eclean-kernel>.

- List all kernel files:

`sudo eclean-kernel {{[-l|--list-kernels]}}`

- Remove all kernels except for the two newest ones:

`sudo eclean-kernel {{[-n|--num]}} 2`

- Remove all kernels except for the two newest ones and ask before removal:

`sudo eclean-kernel {{[-a|--all]}} {{[-n|--num]}} 2`
