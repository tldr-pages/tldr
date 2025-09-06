# aur

> Construye paquetes desde el AUR y gestiona repositorios locales.
> Nota: Es necesario establecer un repositorio local en `/etc/pacman.conf` e instalar `vifm` para que funcione completamente.
> Más información: <https://github.com/aurutils/aurutils>.

- Busca un paquete en la base de datos del AUR:

`aur search {{palabra_clave}}`

- Descarga un paquete y sus dependencias desde el AUR, los compila y añade a un repositorio local:

`aur sync {{paquete}}`

- Lista paquetes disponibles en tu repositorio local:

`aur repo {{[-l|--list]}}`

- Actualiza los paquetes del repositorio local:

`aur sync {{[-u|--upgrades]}}`

- Instala un paquete sin ver los cambios en Vim y sin confirmar la instalación de dependencias:

`aur sync --noview {{[-n|--noconfirm]}} {{paquete}}`
