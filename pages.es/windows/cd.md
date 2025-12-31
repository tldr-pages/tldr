# cd

> Muestra el directorio de trabajo actual o se desplaza a un directorio diferente.
> En PowerShell, este comando es un alias de `Set-Location`. Esta documentación está basada en la versión del símbolo del sistema (`cmd`) de `cd`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Muestra la documentación del comando PowerShell equivalente:

`tldr set-location`

- Muestra la ruta del directorio actual:

`cd`

- Va a un directorio específico en la misma unidad:

`cd {{ruta\al\directorio}}`

- Va a un directorio específico en una uni[d]ad diferente:

`cd /d {{C}}:{{ruta\al\directorio}}`

- Sube al directorio padre del directorio actual:

`cd ..`

- Va al directorio principal del usuario actual:

`cd %userprofile%`

- Va a la raíz de la unidad actual:

`cd \`
