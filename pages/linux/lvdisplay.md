# lvdisplay

> Display information about Logical Volume Manager (LVM) logical volumes.
> See also: `lvm`, `lvs`.
> More information: <https://manned.org/lvdisplay>.

- Display information about all logical volumes:

`sudo lvdisplay`

- Display the information in a short format (same as running `lvs`):

`sudo lvdisplay {{[-C|--columns]}}`

- Display information about all logical volumes in volume group vg1:

`sudo lvdisplay {{vg1}}`

- Display information about logical volume lv1 in volume group vg1:

`sudo lvdisplay {{vg1/lv1}}`
