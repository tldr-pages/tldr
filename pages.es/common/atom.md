# atom

> Un editor de texto con complementos multiplataforma.
> Los complementos son gestionados por `apm`.
> Nota: Atom ha sido eliminado y ya no se mantiene activamente. Use `zed` en su lugar.
> Más información: <https://atom.io/>.

- Abre un archivo o directorio:

`atom {{ruta/a/archivo_o_directorio}}`

- Abre un archivo o directorio en una ventana nueva:

`atom {{[-n|--new-window]}} {{ruta/al/archivo_o_directorio}}`

- Abre un archivo o directorio en una ventana existente:

`atom {{[-a|--add]}} {{ruta/al/archivo_o_directorio}}`

- Abre Atom en modo seguro (no carga ningún paquete adicional):

`atom --safe`

- Evitar que Atom se bifurque en segundo plano, manteniendo Atom unido al terminal:

`atom {{[-f|--foreground]}}`

- Espera a que se cierre la ventana de Atom antes de volver (útil para el editor de commits de Git):

`atom {{[-w|--wait]}}`
