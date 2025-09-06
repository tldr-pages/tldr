# nnn

> Gestor de archivos de terminal interactivo y analizador de uso de disco.
> Vea también: `clifm`, `mc`, `ranger`, `vifm`.
> Más información: <https://github.com/jarun/nnn/wiki/Usage#program-options>.

- Abre el directorio actual (o especifica uno como primer argumento):

`nnn`

- Inicia en modo detallado:

`nnn -d`

- Muestra archivos ocultos:

`nnn -H`

- Abre un marcador existente (definido en la variable de entorno `NNN_BMS`):

`nnn -b {{nombre_del_marcador}}`

- Ordena los archivos por [a]parente uso de disco / uso de [d]isco / [e]xtensión / inve[r]so / tamaño / [t]iempo / [v]ersión:

`nnn -T {{a|d|e|r|s|t|v}}`

- Abre archivos que elijas. Selecciona un archivo y oprime `<o>`, después escribe el nombre del programa con el cual abrirlo:

`nnn -o`
