# git clone

> Clona un repositorio existente.
> Más información: <https://git-scm.com/docs/git-clone>.

- Clona un repositorio existente en un directorio nuevo (el directorio por defecto es el nombre del repositorio):

`git clone {{ubicación_repositorio_remoto}} {{ruta/al/directorio}}`

- Clona un repositorio existente y sus submódulos:

`git clone --recursive {{ubicación_repositorio_remoto}}`

- Clona sólo el directorio `.git` de un repositorio existente:

`git clone --no-checkout {{ubicación_repositorio_remoto}}`

- Clona un repositorio local:

`git clone --local {{ruta/al/repositorio/local}}`

- Clona en silencio:

`git clone --quiet {{ubicación_repositorio_remoto}}`

- Clona un repositorio existente obteniendo sólo los 10 commits más recientes de la rama por defecto (útil para ahorrar tiempo):

`git clone --depth {{10}} {{ubicación_repositorio_remoto}}`

- Clona un repositorio existente buscando sólo una rama específica:

`git clone --branch {{nombre}} --single-branch {{ubicación_repositorio_remoto}}`

- Clona un repositorio existente usando un comando SSH específico:

`git clone --config core.sshCommand="{{ssh -i ruta/a/clave_privada_ssh}}" {{ubicación_repositorio_remoto}}`
