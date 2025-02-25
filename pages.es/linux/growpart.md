# growpart

> Extiende una partición en un disco o imagen de disco para llenar el espacio disponible.
> Más información: <https://github.com/canonical/cloud-utils>.

- Extiende la partición `n` desde `sdX` para llenar el espacio vacío hasta el final del disco o el principio de la siguiente partición:

`growpart {{/dev/sdX}} {{n}}`

- Muestra qué modificaciones se harían al hacer crecer la partición `n` en una imagen de disco:

`growpart --dry-run {{/ruta/a/disco.img}} {{n}}`
