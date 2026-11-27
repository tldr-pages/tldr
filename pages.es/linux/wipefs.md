# wipefs

> Borra firmas de sistemas de archivos, RAID o tablas de particiones de un dispositivo.
> Más información: <https://manned.org/wipefs>.

- Muestra las firmas del dispositivo especificado:

`sudo wipefs {{/dev/sdX}}`

- Borra todos los tipos de firma disponibles de un dispositivo específico sin recursión en las particiones:

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}`

- Borra todos los tipos de firma disponibles del dispositivo y de sus particiones usando un patrón `glob`:

`sudo wipefs {{[-a|--all]}} {{/dev/sdX}}*`

- Simula el borrado de todos los tipos de firma de un dispositivo sin modificarlo realmente:

`sudo wipefs {{[-a|--all]}} {{[-n|--no-act]}} {{/dev/sdX}}`

- Fuerza el borrado, incluso si el sistema de archivos está montado:

`sudo wipefs {{[-a|--all]}} {{[-f|--force]}} {{/dev/sdX}}`
