# octo

> Herramientas de línea de comandos para Octopus Deploy.
> Más información: <https://octopus.com/docs/octopus-rest-api/octo.exe-command-line>.

- Crea un paquete:

`octo pack --id {{package}}`

- Sube un paquete a un repositorio en el servidor de Octopus:

`octo push --package {{package}}`

- Crea una versión:

`octo create-release --project {{project_name}} --packageversion {{version}}`

- Despliega una versión:

`octo deploy-release --project {{project_name}} --packageversion {{version}} --deployto {{environment_name}} --tenant {{deployment_target}}`
