# dnf config-manager

> Gestiona las opciones de configuración y los repositorios de DNF en sistemas basados en Fedora.
> Más información: <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>.

- Añade (y habilita) un repositorio desde una URL:

`dnf config-manager --add-repo={{url_del_repositorio}}`

- Imprime los valores de configuración actuales:

`dnf config-manager --dump`

- Habilita un repositorio específico:

`dnf config-manager {{[--enable|--set-enabled]}} {{identificador_del_repositorio}}`

- Deshabilita repositorios específicos:

`dnf config-manager {{[--disable|--set-disabled]}} {{identificador_del_repositorio1 identificador_del_repositorio2 ...}}`

- Establece una opción de configuración para un repositorio:

`dnf config-manager --setopt={{opción}}={{valor}}`

- Muestra la ayuda:

`dnf config-manager --help-cmd`
