# reg export

> Exportar las subclaves y valores especificados a un archivo `.reg`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-export>.

- Exportar todas las subclaves y valores de una clave específica:

`reg export {{nombre_clave}} {{ruta\al\archivo.reg}}`

- Forzar (asumiendo sí [y]) la sobrescritura de un archivo existente:

`reg export {{nombre_clave}} {{ruta\al\archivo.reg}} /y`
