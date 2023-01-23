# lvdisplay

> A Logical Volume Manager (LVM) logikai kötetekről szóló információk megjelenítése. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvdisplay.8.html>.

- Az összes logikai kötetre vonatkozó információk megjelenítése:

`sudo lvdisplay`

- A vg1 kötetcsoportban lévő összes logikai kötetre vonatkozó információk megjelenítése:

`sudo lvdisplay {{vg1}}`

- A vg1 kötetcsoportban lévő lv1 logikai kötetre vonatkozó információk megjelenítése:

`sudo lvdisplay {{vg1/lv1}}`
