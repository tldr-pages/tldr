# a2query

> Recupera la configuración en tiempo de ejecución de Apache en sistemas operativos basados en Debian.
> Más información: <https://manpages.debian.org/latest/apache2/a2query.html>.

- Lista módulos de Apache habilitados:

`sudo a2query -m`

- Comprueba si un módulo específico está instalado:

`sudo a2query -m {{nombre_del_módulo}}`

- Lista hosts virtuales habilitados:

`sudo a2query -s`

- Muestra el Módulo de Procesamiento Múltiple actualmente habilitado:

`sudo a2query -M`

- Muestra la versión de Apache:

`sudo a2query -v`
