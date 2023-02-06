# lvremove

> Egy vagy több logikai kötet eltávolítása. Lásd még: `lvm`. További információ: <https://man7.org/linux/man-pages/man8/lvremove.8.html>.

- Logikai kötet eltávolítása egy kötetcsoportban:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Egy kötetcsoport összes logikai kötetének eltávolítása:

`sudo lvremove {{volume_group}}`
