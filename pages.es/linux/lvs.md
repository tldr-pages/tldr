# lvs

> Imprime información sobre volúmenes lógicos.
> Vea también: `lvm`.
> Más información: <https://manned.org/lvs>.

- Muestra información sobre volúmenes lógicos:

`lvs`

- Muestra todos los volúmenes lógicos:

`lvs {{[-a|--all]}}`

- Cambia la visualización por defecto para mostrar más detalles:

`lvs {{[-v|--verbose]}}`

- Muestre solo campos especificos:

`lvs {{[-o|--options]}} {{nombre_campo_1}},{{nombre_campo_2}}`

- Añade un campo a la visualización por defecto:

`lvs {{[-o|--options]}} +{{nombre_campo}}`

- Suprime linea de encabezado:

`lvs --noheadings`

- Usa un separador para separar los campos:

`lvs --separator {{=}}`
