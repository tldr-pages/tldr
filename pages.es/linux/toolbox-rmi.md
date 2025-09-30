# toolbox rmi

> Elimina imágenes de `toolbox`.
> Vea también: `toolbox rm`.
> Más información: <https://manned.org/toolbox-rmi.1>.

- Quita una o más imágenes de `toolbox`:

`toolbox rmi {{nombre_de_la_imagen1 nombre_de_la_imagen2 ...}}`

- Quita todas las imágenes de `toolbox`:

`toolbox rmi --all`

- Fuerza la eliminación de una imagen de `toolbox` que está siendo utilizado actualmente por un contenedor (el contenedor será eliminado también):

`toolbox rmi --force {{nombre_de_la_imagen}}`
