# az bicep

> Grupo de comandos de la CLI de Bicep.
> Parte de `azure-cli`.
> Más información: <https://learn.microsoft.com/cli/azure/bicep>.

- Instala la CLI de Bicep.

`az bicep install`

- Crear un archivo de Bicep:

`az bicep build --file {{ruta/al/archivo.bicep}}`

- Intenta descompilar un archivo de plantilla ARM a un archivo de Bicep:

`az bicep decompile --file {{ruta/al/archivo_plantilla.json}}`

- Actualiza la CLI de Bicep a la última versión:

`az bicep upgrade`

- Muestra la versión instalada de la CLI de Bicep:

`az bicep version`

- Lista todas las versiones disponibles de la CLI de Bicep:

`az bicep list-versions`

- Desinstala la CLI de Bicep:

`az bicep uninstall`
