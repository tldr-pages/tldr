# trash

> Gestiona el contenedor de basura/reciclaje.
> Más información: <https://github.com/andreafrancia/trash-cli>.

- Envía un archivo a la basura:

`trash {{ruta/al/archivo}}`

- Lista todos los archivos en la basura:

`trash-list`

- Restaura interactivamente un archivo de la basura:

`trash-restore`

- Vacía la basura:

`trash-empty`

- Elimina permanentemente todos los archivos en la basura mayores a 10 días:

`trash-empty 10`

- Elimina todos los archivos en la basura, que coinciden con un patrón blob específico:

`trash-rm "{{*.o}}"`

- Elimina todos los archivos con una ubicación original específica:

`trash-rm {{/ruta/al/archivo_o_directorio}}`
