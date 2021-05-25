# git config

> Gestiona opciones personalizadas para la configuración de repositorios Git.
> Estas configuraciones pueden ser locales (para el repositorio actual) o globales (para el usuario actual).
> Más información: <https://git-scm.com/docs/git-config>.

- Muestra solo las entradas de la configuración local (almacenadas en `.git/config` en el repositorio actual):

`git config --list --local`

- Muestra solo las entradas de la configuración global (almacenadas en `~/.gitconfig`):

`git config --list --global`

- Muestra todas las entradas de configuración que han sido definidas local o globalmente:

`git config --list`

- Muestra el valor de una entrada específica de la configuración:

`git config alias.unstage`

- Establece el valor global para una entrada específica de la configuración:

`git config --global alias.unstage "reset HEAD --"`

- Revierte una entrada de la configuración global a su valor por defecto:

`git config --global --unset alias.unstage`

- Edita la configuración de Git para el repositorio actual en el editor por defecto:

`git config --edit`

- Edita la configuración global de Git en el editor por defecto:

`git config --global --edit`
