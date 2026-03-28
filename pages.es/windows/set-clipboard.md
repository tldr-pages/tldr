# Set-Clipboard

> Comando de PowerShell para copiar contenido al portapapeles.
> Nota: Se puede utilizar `scb` como alias de `Set-Clipboard`.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/set-clipboard>.

- Copia texto al portapapeles:

`Set-Clipboard -Value "{{texto}}"`

- Copia varios textos al portapapeles separados por una nueva línea:

`Set-Clipboard -Value @("{{texto 1}}", "{{texto 2}}", "{{texto 3}}")`

- Copia archivos o directorios al portapapeles:

`Set-Clipboard -Path "{{ruta\a\archivos_o_directorios}}"`

- Copia varios archivos:

`Set-Clipboard -Path "{{ruta\a\archivo1}}", "{{ruta\a\archivo2}}", "{{ruta\a\archivo3}}"`

- Limpia el portapapeles:

`Set-Clipboard ""`
