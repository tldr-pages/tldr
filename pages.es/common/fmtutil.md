# fmtutil

> Gestiona formatos TeX y bases Metafont.
> Más información: <https://manned.org/fmtutil>.

- Vuelve a generar todos los archivos de formato:

`fmtutil --all`

- Crea todos los archivos de formato que falten:

`fmtutil --missing`

- Muestra una lista de las configuraciones de formato disponibles:

`fmtutil --listcfg`

- Vuelve a crear formatos generados con un motor específico:

`fmtutil --byengine {{motor}}`

- Vuelve a crear un formato específico:

`fmtutil --byfmt {{formato}}`

- Vuelve a crear todos los archivos de formato del sistema:

`fmtutil --sys --all`

- Vuelve a crear todos los archivos de formato de usuario:

`fmtutil --user --all`
