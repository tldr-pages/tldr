# toolbox rmi

> Elimina imágenes de Toolbx.
> Vea también: `toolbox rm`.
> Más información: <https://manned.org/toolbox-rmi.1>.

- Quita una o más imágenes de Toolbx:

`toolbox rmi {{nombre_de_la_imagen1 nombre_de_la_imagen2 ...}}`

- Quita todas las imágenes de Toolbx:

`toolbox rmi --all`

- Fuerza la eliminación de una imagen de Toolbx que está siendo utilizada actualmente por un contenedor (el contenedor será eliminado también):

`toolbox rmi --force {{nombre_de_la_imagen}}`
