# lvremove

> Eliminați unul sau mai multe volume logice.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvremove.8.html>

- Eliminați un volum logic într-un grup de volum:

`sudo lvremove {{volume_group}}/{{logical_volume}}`

- Eliminați toate volumele logice dintr-un grup de volum:

`sudo lvremove {{volume_group}}`
