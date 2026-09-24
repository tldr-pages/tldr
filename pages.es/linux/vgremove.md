# vgremove

> Elimina grupo(s) de volúmenes en LVM.
> Más información: <https://manned.org/vgremove>.

- Elimina un grupo de volúmenes con confirmación:

`sudo vgremove {{grupo_volumen}}`

- Fuerza la eliminación de un grupo de volúmenes sin confirmación:

`sudo vgremove {{[-f|--force]}} {{grupo_volumen}}`

- Establece el nivel de depuración para el registro detallado en el nivel 2, (repite `--debug` hasta 6 veces para aumentar el nivel):

`sudo vgremove {{[-d|--debug]}} {{[-d|--debug]}} {{grupo_volumen}}`

- Utiliza una configuración específica para anular los valores predeterminados:

`sudo vgremove --config '{{global/locking_type=1}}' {{grupo_volumen}}`

- Muestra texto de ayuda para obtener información de uso:

`vgremove {{[-h|--help]}}`
