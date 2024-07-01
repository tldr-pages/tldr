# portageq

> Consulta información sobre Portage, el gestor de paquetes de Gentoo Linux.
> Las variables de entorno específicas de Portage que se pueden consultar están listadas en `/var/db/repos/gentoo/profiles/info_vars`.
> Más información: <https://wiki.gentoo.org/wiki/Portageq>.

- Muestra el valor de una variable de entorno específica de Portage:

`portageq envvar {{variable}}`

- Muestra una lista detallada de los repositorios configurados con Portage:

`portageq repos_config /`

- Muestra una lista de repositorios ordenados por prioridad (el más alto, primero):

`portageq get_repos /`

- Muestra un fragmento específico de metadatos sobre un átomo (por ejemplo, el nombre del paquete incluyendo la versión):

`portageq metadata / {{ebuild|porttree|binary|...}} {{categoría}}/{{paquete}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`
