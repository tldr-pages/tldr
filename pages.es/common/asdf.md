# asdf

> Gestiona las versiones de diferentes paquetes.
> Más información: <https://asdf-vm.com/manage/commands.html>.

- Muestra todos los complementos disponibles:

`asdf plugin list all`

- Instala un complemento:

`asdf plugin add {{nombre}}`

- Muestra todas las versiones disponibles de un paquete:

`asdf list all {{nombre}}`

- Instala una versión específica de un paquete:

`asdf install {{nombre}} {{versión}}`

- Establece la versión global de un paquete:

`asdf set -u {{nombre}} {{versión}}`

- Establece la versión local de un paquete:

`asdf set {{nombre}} {{versión}}`

- Ver la versión actual utilizada por un paquete:

`asdf current {{nombre}}`
