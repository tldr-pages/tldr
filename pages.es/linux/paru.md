# paru

> Un asistente del AUR y envoltorio para pacman.
> Más información: <https://github.com/Morganamilo/paru>.

- Busca e instala un paquete de forma interactiva:

`paru {{nombre_del_paquete_o_término_de_búsqueda}}`

- Sincroniza y actualiza todos los paquetes:

`paru`

- Actualiza paquetes del AUR:

`paru -Sua`

- Obtiene información acerca del paquete:

`paru -Si {{paquete}}`

- Descarga `PKGBUILD` y otros archivos fuente del paquete desde AUR o ABS:

`paru --getpkgbuild {{paquete}}`

- Muestra el archivo `PKGBUILD` de un paquete:

`paru --getpkgbuild --print {{paquete}}`
