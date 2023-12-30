# git config

> Gestiona opciones de configuración personalizadas para repositorios Git.
> Estas configuraciones pueden ser locales (para el repositorio actual) o globales (para el usuario actual).
> Más información: <https://git-scm.com/docs/git-config>.

- Lista sólo las entradas de configuración local (almacenadas en `.git/config` en el repositorio actual):

`git config --list --local`

- Lista sólo las entradas de configuración global (almacenadas en `~/.gitconfig` por defecto o en `$XDG_CONFIG_HOME/git/config` si existe tal archivo):

`git config --list --global`

- Lista sólo las entradas de configuración del sistema (almacenadas en `/etc/gitconfig`), y muestra su ubicación:

`git config --list --system --show-origin`

- Obtiene el valor de una entrada de configuración dada:

`git config alias.unstage`

- Establece el valor global de una entrada de configuración dada:

`git config --global alias.unstage "reset HEAD --"`

- Revierte una entrada de configuración global a su valor por defecto:

`git config --global --unset alias.unstage`

- Edita la configuración de Git para el repositorio actual en el editor por defecto:

`git config --edit`

- Edita la configuración global de Git en el editor por defecto:

`git config --global --edit`
