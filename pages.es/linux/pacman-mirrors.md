# pacman-mirrors

> Genera una lista de réplicas de `pacman` para Manjaro Linux.
> Cada vez que se ejecute `pacman-mirrors`, es necesario sincronizar la base de datos y actualizar el sistema con `sudo pacman -Syyu`.
> Vea también: `pacman`.
> Más información: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Genera una lista de réplicas utilizando la configuración predeterminada:

`sudo pacman-mirrors --fasttrack`

- Obtiene el estado de las réplicas actuales:

`pacman-mirrors --status`

- Muestra la rama actual:

`pacman-mirrors --get-branch`

- Cambia a una rama diferente:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Genera una lista de servidores de réplicas utilizando únicamente los de tu país:

`sudo pacman-mirrors --geoip`
