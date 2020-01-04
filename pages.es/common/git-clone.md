# git clone

> Clona un repositorio existente.
> Más información: <https://git-scm.com/docs/git-clone>.

- Clona un repositorio existente:

`git clone {{ubicación_remota_del_repositorio}}`

- Clona un repositorio existente y sus submódulos:

`git clone --recursive {{ubicación_remota_del_repositorio}}`

- Clona un repositorio local:

`git clone -l {{ruta/del/repositorio/local}}`

- Clona silenciosamente (sin detalles del proceso de clonación):

`git clone -q {{ubicación_remota_del_repositorio}}`

- Clona un repositorio existente a partir de los últimos 10 commits más reciente de la rama por defecto (útil para ahorrar tiempo):

`git clone --depth {{10}} {{ubicación_remota_del_repositorio}}`
