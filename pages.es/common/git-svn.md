# git svn

> Operacion bidreccional entre un repositorio Subversión y otro Git.
> Mas información: <https://git-scm.com/docs/git-svn>.

- Clona un repositorio SVN:

`git svn clone {{https://ejemplo.com/repositorio_subversion}} {{directorio_local}}`

- Clona un repositorio SVN a partir un número de revisión específico:

`git svn clone -r{{1234}}:HEAD {{https://svn.ejemplo.net/subversion/repo}} {{directorio_local}}`

- Actualiza el clon local apartir del repositorio SVN:

`git svn rebase`

- Obtiene las actualización del repositorio SVN remoto sin cambiar el HEAD de git:

`git svn fetch`

- Realiza un commit al repositorio SVN:

`git svn dcommit`
