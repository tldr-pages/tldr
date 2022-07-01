# git clone

> Clona un repositorio existente.
> Más información: <https://git-scm.com/docs/git-clone>.

- Clona un repositorio existente:

`git clone {{ubicacion_remota_del_repositorio}}`

- Clona un repositorio existente en un directorio específico:

`git clone {{ubicacion_remota_del_repositorio}} {{ruta/al/directorio}}`

- Clona un repositorio existente y sus submódulos:

`git clone --recursive {{ubicacion_remota_del_repositorio}}`

- Clona un repositorio local:

`git clone -l {{ruta/al/repositorio/local}}`

- Clona silenciosamente:

`git clone -q {{ubicacion_remota_del_repositorio}}`

- Clona un repositorio existente solo descargando los 10 commits más recientes de la rama por defecto (útil para ahorrar tiempo):

`git clone --depth {{10}} {{ubicacion_remota_del_repositorio}}`

- Clona un repositorio existente solo descargando un branch específico:

`git clone --branch {{nombre}} --single-branch {{ubicacion_remota_del_repositorio}}`

- Clona un repositorio existente usando un comando SSH específico:

`git clone --config core.sshCommand="{{ssh -i ruta/a/clave_ssh_privada}}" {{ubicacion_remota_del_repositorio}}`
