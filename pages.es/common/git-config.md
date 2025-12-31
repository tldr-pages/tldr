# git config

> Gestiona opciones de configuración personalizadas para repositorios Git.
> Estas configuraciones pueden ser locales (para el repositorio actual) o globales (para el usuario actual).
> Más información: <https://git-scm.com/docs/git-config>.

- Establece globalmente tu nombre o correo electrónico (esta información es necesaria para hacer un commit en un repositorio y se incluirá en todos los commits):

`git config --global {{user.name|user.email}} "{{Tu nombre|email@example.com}}"`

- Lista las entradas de configuración local o global:

`git config {{[-l|--list]}} --{{local|global}}`

- Lista sólo las entradas de configuración del sistema (almacenadas en `/etc/gitconfig`), y muestra la ubicación de dicho archivo:

`git config {{[-l|--list]}} --system --show-origin`

- Obtén el valor de una entrada de configuración dada:

`git config alias.unstage`

- Establece el valor global de una entrada de configuración dada:

`git config --global alias.unstage "reset HEAD --"`

- Revierte una entrada de configuración global a su valor por defecto:

`git config --global --unset alias.unstage`

- Edita la configuración local de Git (`.git/config`) en el editor por defecto:

`git config {{[-e|--edit]}}`

- Edita la configuración global de Git (`~/.gitconfig` por defecto o `$XDG_CONFIG_HOME/git/config` si existe tal archivo) en el editor por defecto:

`git config --global {{[-e|--edit]}}`
