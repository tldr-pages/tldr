# dnf config-manager

> Administra opciones de configuración y repositorios DNF en sistemas basados en Fedora.
> Más información: <https://manned.org/dnf-config-manager>.

- Agrega (y activa) un repositorio de una URL:

`dnf config-manager --add-repo={{url_del_repositorio}}`

- Imprime los valores de configuración actuales:

`dnf config-manager --dump`

- Habilita un repositorio específico:

`dnf config-manager --set-enabled {{identificador_del_repositorio}}`

- Deshabilita repositorios especificados:

`dnf config-manager --set-disabled {{identificador_del_repositorio1 identificador_del_repositorio2 ...}}`

- Establece una opción de configuración para un repositorio:

`dnf config-manager --setopt={{opción}}={{valor}}`

- Muestra la ayuda:

`dnf config-manager --help-cmd`
