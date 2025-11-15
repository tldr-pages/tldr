# Remove-Item

> Elimina archivos, carpetas, así como claves de registro y subclaves.
> Este comando solo se puede ejecutar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/remove-item>.

- Elimina archivos específicos o claves de registro (sin subclaves):

`Remove-Item {{ruta\al\archivo_o_clave1 , ruta\al\archivo_o_clave2 ...}}`

- Elimina archivos ocultos o de solo lectura:

`Remove-Item -Force {{ruta\al\archivo1 , ruta\al\archivo2 ...}}`

- Elimina archivos específicos o claves de registro de forma interactiva antes de cada eliminación:

`Remove-Item -Confirm {{ruta\al\archivo_o_clave1 , ruta\al\archivo_o_clave2 ...}}`

- Elimina archivos y directorios específicos recursivamente (Windows 10 versión 1909 o posterior):

`Remove-Item -Recurse {{ruta\al\archivo_o_directorio1 , ruta\al\archivo_o_directorio2 ...}}`

- Quita claves específicas del registro de Windows y todas sus subclaves:

`Remove-Item -Recurse {{ruta\a\la\clave1 , ruta\a\la\clave2 ...}}`

- Realiza una simulación del proceso de eliminación:

`Remove-Item -WhatIf {{ruta\al\archivo1 , ruta\al\archivo2 ...}}`
