# a2query

> Recuperar la configuración del tiempo de ejecución de Apache en sistemas operativos basados en Debian.
> Más información: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Lista de módulos de Apache habilitados:

`sudo a2query -m`

- Comprobar si un módulo específico está instalado:

`sudo a2query -m {{nombre_del_módulo}}`

- Lista de hosts virtuales habilitados:

`sudo a2query -s`

- Mostrar el Módulo de Procesamiento Múltiple habilitado actualmente:

`sudo a2query -M`

- Mostrar la versión de Apache:

`sudo a2query -v`
