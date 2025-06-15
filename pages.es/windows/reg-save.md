# reg save

> Guarda una clave del registro, sus subclaves y valores en un archivo `.hiv` nativo.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- Guardar una clave del registro, sus subclaves y valores en un archivo específico:

`reg save {{nombre_de_clave}} {{ruta\al\archivo.hiv}}`

- Sobrescribir forzosamente (asumiendo sí [y]) un archivo existente:

`reg save {{nombre_de_clave}} {{ruta\al\archivo.hiv}} /y`
