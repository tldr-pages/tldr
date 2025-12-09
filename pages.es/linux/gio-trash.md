# gio trash

> Mueve archivos a la papelera.
> Usado por GNOME para manejar la papelera.
> Más información: <https://manned.org/gio.1>.

- Mueve archivos específicos a la papelera:

`gio trash {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Lista los elementos de la papelera:

`gio trash --list`

- Restaura un elemento específico de la papelera utilizando su identificador:

`gio trash trash://{{identificador}}`
