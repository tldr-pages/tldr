# aurman

> Una utilidad de Arch Linux para construir e instalar paquetes desde el repositorio de usuarios de Arch (AUR).
> Vea también: `pacman`.
> Más información: <https://github.com/polygamma/aurman#syntax>.

- Sincroniza y actualiza todos los paquetes:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}}`

- Sincroniza y actualiza todos los paquetes sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman {{[-S|--sync]}} {{[-y|--refresh]}} {{[-u|--sysupgrade]}} --noedit`

- Instala un nuevo paquete:

`aurman {{[-S|--sync]}} {{paquete}}`

- Instala un nuevo paquete sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman {{[-S|--sync]}} --noedit {{paquete}}`

- Instala un nuevo paquete sin pedir confirmación:

`aurman {{[-S|--sync]}} --noedit --noconfirm {{paquete}}`

- Busca en la base de datos de paquetes una palabra clave en los repositorios oficiales y AUR:

`aurman {{[-S|--sync]}} {{[-s|--search]}} {{palabra_clave}}`

- Elimina un paquete y sus dependencias:

`aurman --remove --recursive --nosave {{paquete}}`

- Limpia la caché de paquetes (usa dos banderas `--clean` para limpiar todos los paquetes):

`aurman {{[-S|--sync]}} {{[-c|--clean]}}`
