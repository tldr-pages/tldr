# aurvote

> Vota por paquetes en el repositorio de usuarios de Arch (AUR).
> Para poder votar, el archivo `~/.config/aurvote` debe existir y contener tus credenciales del AUR.
> Más información: <https://github.com/archlinuxfr/aurvote>.

- Crea interactivamente el archivo `~/.config/aurvote` que contiene su nombre de usuario y contraseña del AUR:

`aurvote --configure`

- Vota por uno o más paquetes del AUR:

`aurvote {{paquete1 paquete2 ...}}`

- Retira el voto de uno o más paquetes del AUR:

`aurvote --unvote {{paquete1 paquete2 ...}}`

- Verifica si uno o más paquetes del AUR ya han sido votados:

`aurvote --check {{paquete1 paquete2 ...}}`

- Muestra la ayuda:

`aurvote --help`
