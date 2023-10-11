# bless

> Establece la capacidad de arranque del volumen y las opciones del disco de arranque.
> Más información: <https://ss64.com/osx/bless.html>.

- Bendice un volumen sólo con Mac OS X o Darwin, y crea los archivos BootX y `boot.efi` según sea necesario:

`bless --folder {{/Volumes/Mac OS X/System/Library/CoreServices}} --bootinfo --bootefi`

- Configura un volumen que contenga Mac OS 9 y Mac OS X para que sea el volumen activo:

`bless --mount {{Volumes/Mac OS}} --setBoot`

- Configura el sistema como NetBoot y localiza un servidor disponible:

`bless --netboot --server {{bsdp://255.255.255.255}}`

- Recopila información sobre el volumen seleccionado actualmente (según lo determinado por el firmware), adecuado para la canalización a un programa capaz de analizar las listas de propiedades:

`bless --info --plist`
