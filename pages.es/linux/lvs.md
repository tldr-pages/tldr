# lvs

> Imprime información sobre volúmenes lógicos.
> Vea también: `lvm`.
> Más información: <https://manned.org/lvs>.

- Muestra información sobre volúmenes lógicos:

`sudo lvs`

- Muestra todos los volúmenes lógicos:

`sudo lvs {{[-a|--all]}}`

- Cambia la visualización por defecto para mostrar más detalles:

`sudo lvs {{[-v|--verbose]}}`

- Muestre solo campos especificos:

`sudo lvs {{[-o|--options]}} {{nombre_campo_1,nombre_campo_2,...}}`

- Añade un campo a la visualización por defecto:

`sudo lvs {{[-o|--options]}} +{{nombre_campo}}`

- Suprime linea de encabezado:

`sudo lvs --noheadings`

- Usa un separador para separar los campos:

`sudo lvs --separator {{=}}`
