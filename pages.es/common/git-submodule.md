# git submodule

> Inspecciona, actualiza y gestiona los submódulos.
> Más información: <https://git-scm.com/docs/git-submodule>.

- Instala los submódulos específicos de un repositorio:

`git submodule update --init --recursive`

- Añade un repositorio como un submódulo:

`git submodule add {{url_del_repositorio}}`

- Añade un repositorio Git como submódulo en un directorio específico:

`git submodule add {{url_del_repositorio}} {{ruta/al/directorio}}`

- Actualiza cada submódulo a su último commit:

`git submodule foreach git pull`
