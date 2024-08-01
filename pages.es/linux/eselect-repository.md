# eselect repository

> Un módulo `eselect` para configurar repositorios ebuild para Portage.
> Después de habilitar un repositorio, tienes que ejecutar `emerge --sync repo_name` para descargar ebuilds.
> Más información: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- Lista todos los repositorios ebuild registrados en <https://repos.gentoo.org>:

`eselect repository list`

- Lista de repositorios habilitados:

`eselect repository list -i`

- Habilita un repositorio de la lista según su nombre o índice desde el comando `list`:

`eselect repository enable {{name|index}}`

- Activa un repositorio no registrado:

`eselect repository add {{nombre}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- Deshabilita repositorios sin eliminar su contenido:

`eselect repository disable {{repo1 repo2 ...}}`

- Desactiva repositorios y elimina su contenido:

`eselect repository remove {{repo1 repo2 ...}}`

- Crea un repositorio local y lo habilita:

`eselect repository create {{nombre}} {{ruta/al/repo}}`
