# git init

> Inicializa un nuevo repositorio Git local.
> Más información: <https://git-scm.com/docs/git-init>.

- Inicializa un nuevo repositorio local:

`git init`

- Inicializa un repositio usando SHA256 como hash del objeto (requiere la versión 2.29+ de Git):

`git init --object-format={{sha256}}`

- Inicializa un repositorio vacío, adecuado para usarlo como remoto a través de ssh:

`git init --bare`
