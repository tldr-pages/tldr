# lvdisplay

> Imprime información sobre Logical Volumes Manager(LVM).
> Ver: `lvm`.
> Mas Informacion: <https://manned.org/lvdisplay>.

- Mostrar informacion sobre todos los volumenes logicos:

`sudo lvdisplay`

- Mostrar informacion sobre todos los volumenes logicos dentro del grupo de volumenes vg1:

`sudo lvdisplay {{vg1}}`

- Mostrar informacion sobre volumen logico lv1 dentro del grupo de volumenes vg1:

`sudo lvdisplay {{vg1/lv1}}`
