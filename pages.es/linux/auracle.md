# auracle

> Herramienta de línea de comandos utilizada para interactuar con el repositorio de usuarios de Arch Linux, comúnmente conocido como AUR.
> Más información: <https://github.com/falconindy/auracle/blob/master/man/auracle.1.pod>.

- Muestra los paquetes del AUR que coinciden con una expresión regular:

`auracle search '{{expresión_regular}}'`

- Muestra información sobre uno o más paquetes del AUR:

`auracle info {{paquete1 paquete2 ...}}`

- Muestra el archivo `PKGBUILD` (información de construcción) de uno o más paquetes del AUR:

`auracle show {{paquete1 paquete2 ...}}`

- Muestra actualizaciones para los paquetes del AUR instalados:

`auracle outdated`
