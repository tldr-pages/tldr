# powershell

> Shell de línea de comandos y lenguaje de scripting diseñado especialmente para la administración del sistema.
> Este comando se refiere a la versión 5.1 de PowerShell y anteriores (también conocida como Windows PowerShell heredada). Para usar la versión más nueva y multiplataforma de PowerShell (también conocida como PowerShell Core), usa `pwsh` en lugar de `powershell`.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/powershell>.

- Iniciar una sesión interactiva de shell:

`powershell`

- Iniciar una sesión interactiva de shell sin cargar configuraciones de inicio:

`powershell -NoProfile`

- Ejecutar comandos específicos:

`powershell -Command "{{echo 'powershell se está ejecutando'}}"`

- Ejecutar un script específico:

`powershell -File {{ruta/al/script.ps1}}`

- Iniciar una sesión con una versión específica de PowerShell:

`powershell -Version {{versión}}`

- Evitar que el shell se cierre después de ejecutar comandos de inicio:

`powershell -NoExit`

- Describir el formato de los datos enviados a PowerShell:

`powershell -InputFormat {{Texto|XML}}`

- Determinar cómo se formatea una salida de PowerShell:

`powershell -OutputFormat {{Texto|XML}}`
