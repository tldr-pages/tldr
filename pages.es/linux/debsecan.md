# debsecan

> Analizador de seguridad de Debian, es una herramienta para enumerar vulnerabilidades en una instalación Debian en particular.
> Más información: <https://manned.org/debsecan>.

- Lista de paquetes instalados vulnerables en el host actual:

`debsecan`

- Lista de paquetes instalados vulnerables de una versión específica:

`debsecan --suite {{nombre_de_la_versión}}`

- Lista solo vulnerabilidades arregladas:

`debsecan --suite {{nombre_de_la_versión}} --only-fixed`

- Lista solo vulnerabilidades arregladas de inestable ("sid") y envía un correo a root:

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- Actualiza paquetes vulnerables instalados:

`sudo apt upgrade $(debsecan --only-fixed --format {{paquetes}})`
