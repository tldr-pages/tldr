# octo

> Herramientas de línea de comandos para Octopus Deploy.
> Más información: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- Crea un paquete:

`octo pack --id={{paquete}}`

- Sube un paquete a un repositorio en el servidor de Octopus:

`octo push --package={{paquete}}`

- Crea una versión:

`octo create-release --project={{nombre_del_proyecto}} --packageversion={{versión}}`

- Despliega una versión:

`octo deploy-release --project={{nombre_del_proyecto}} --packageversion={{versión}} --deployto={{nombre_del_entorno}} --tenant={{objetivo_de_despliegue}}`
