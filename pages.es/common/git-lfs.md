# git lfs

> Trabaja con archivos grandes en repositorios de Git.
> Más información: <https://git-lfs.com>.

- Inicializa Git LFS:

`git lfs install`

- Rastrea archivos que coinciden con un patrón:

`git lfs track '{{*.bin}}'`

- Cambia la URL a la que apunta Git LFS (útil si el servidor LFS está separado del servidor Git):

`git config -f .lfsconfig lfs.url {{url_del_punto_de_acceso_LFS}}`

- Muestra los patrones rastreados:

`git lfs track`

- Muestra los archivos que han sido añadidos con un commit:

`git lfs ls-files`

- Introduce todos los objetos LFS en el servidor remoto (útil si se encuentran errores):

`git lfs push --all {{nombre_remoto}} {{nombre_de_la_rama}}`

- Trae todos los objetos de Git LFS:

`git lfs fetch`

- Verifica todos los objetos de Git LFS:

`git lfs checkout`
