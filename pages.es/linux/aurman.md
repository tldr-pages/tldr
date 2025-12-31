# aurman

> Una utilidad de Arch Linux para construir e instalar paquetes desde el repositorio de usuarios de Arch (AUR).
> Vea también: `pacman`.
> Más información: <https://github.com/polygamma/aurman#syntax>.

- Sincroniza y actualiza todos los paquetes:

`aurman --sync --refresh --sysupgrade`

- Sincroniza y actualiza todos los paquetes sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman --sync --refresh --sysupgrade --noedit`

- Instala un nuevo paquete:

`aurman --sync {{paquete}}`

- Instala un nuevo paquete sin mostrar los cambios en los archivos `PKGBUILD`:

`aurman --sync --noedit {{paquete}}`

- Instala un nuevo paquete sin pedir confirmación:

`aurman --sync --noedit --noconfirm {{paquete}}`

- Busca en la base de datos de paquetes una palabra clave en los repositorios oficiales y AUR:

`aurman --sync --search {{palabra_clave}}`

- Elimina un paquete y sus dependencias:

`aurman --remove --recursive --nosave {{paquete}}`

- Limpia la caché de paquetes (usa dos banderas `--clean` para limpiar todos los paquetes):

`aurman --sync --clean`
