# lvdisplay

> Display information about Logical Volume Manager (LVM) logical volumes.
> See also: `lvm`.
> More information: <https://man7.org/linux/man-pages/man8/lvdisplay.8.html>.

- Display information about all logical volumes:

`sudo lvdisplay`

- Display information about all logical volumes in volume group vg1:

`sudo lvdisplay {{vg1}}`

- Display information about logical volume lv1 in volume group vg1:

`sudo lvdisplay {{vg1/lv1}}`
