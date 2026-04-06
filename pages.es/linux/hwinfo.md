# hwinfo

> Detecta el hardware presente en el sistema.
> Vea también: `inxi`, `lshw`, `dmidecode`.
> Más información: <https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>.

- Muestra toda la información disponible sobre el hardware:

`hwinfo`

- Muestra información sobre un componente de hardware específico:

`hwinfo --{{cpu|memory|disk|gfxcard|network|usb|pci|keyboard|mouse|monitor|sound|fingerprint|...}}`

- Muestra información sobre un componente de hardware específico de forma concisa:

`hwinfo {{--componente}} --short`

- Escribe toda la información del hardware en un archivo:

`hwinfo --all --log {{ruta/al/archivo}}`

- Muestra la ayuda:

`hwinfo --help`
