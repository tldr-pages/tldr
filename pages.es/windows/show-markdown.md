# Show-Markdown

> Muestra un archivo o cadena Markdown en la consola de forma amigable usando secuencias de escape VT100 o en un navegador usando HTML.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/show-markdown>.

- Renderizar markdown en la consola desde un archivo:

`Show-Markdown -Path {{ruta\al\archivo}}`

- Renderizar markdown en la consola desde una cadena:

`"{{# Contenido Markdown}}" | Show-Markdown`

- Abrir archivo Markdown en un navegador:

`Show-Markdown -Path {{ruta\al\archivo}} -UseBrowser`
