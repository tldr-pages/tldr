# pvcreate

> Inițializați un disc sau o partiție pentru utilizare ca volum fizic.
> A se vedea, de asemenea: `lvm`.
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/pvcreate.8.html>

- Iniţializaţi volumul `/dev/sda1` pentru utilizarea de către LVM:

`pvcreate {{/dev/sda1}}`

- Forțați crearea fără nici o confirmare a solicitării:

`pvcreate --force {{/dev/sda1}}`
