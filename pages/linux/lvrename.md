# lvrename

> lvrename renames an existing LV or a historical LV.
> More information: <https://manned.org/man/lvrename>.

- Rename a logical volume:

`lvrename`

- Rename "lvold" to "lvnew":

`lvrename /dev/vg02/lvold vg02/lvnew`

- An alternate syntax to rename "lvold" to "lvnew"::

`lvrename vg02 lvold lvnew`
