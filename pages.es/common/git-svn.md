# git svn

> Operacion bidreccional entre un repositorio Subversión y otro Git.
> Más información: <https://git-scm.com/docs/git-svn>.

- Clona un repositorio SVN:

`git svn clone {{https://ejemplo.com/repositorio_subversion}} {{directorio_local}}`

- Clona un repositorio SVN a partir un número de revisión específico:

`git svn clone -r{{1234}}:HEAD {{https://svn.ejemplo.net/subversion/repo}} {{directorio_local}}`

- Actualiza el clon local a partir del repositorio SVN:

`git svn rebase`

- Obtén las actualizaciones del repositorio SVN remoto sin cambiar el HEAD de Git:

`git svn fetch`

- Realiza una confirmación en un repositorio SVN:

`git svn commit`
