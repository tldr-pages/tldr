# Set-Volume

> Establece o cambia la etiqueta del sistema de archivos de un volumen existente.
> Nota: Este comando solo puede usarse a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/storage/set-volume>.

- Cambiar la etiqueta del sistema de archivos de un volumen identificado por la letra de unidad:

`Set-Volume -DriveLetter "D" -NewFileSystemLabel "VolumenDatos"`

- Cambiar la etiqueta del sistema de archivos de un volumen identificado por la etiqueta del sistema:

`Set-Volume -FileSystemLabel "EtiquetaVieja" -NewFileSystemLabel "EtiquetaNueva"`

- Modificar las propiedades de un volumen usando un objeto volumen:

`Set-Volume -InputObject $(Get-Volume -DriveLetter "E") -NewFileSystemLabel "Respaldo"`

- Especificar el modo de desduplicación de datos para el volumen:

`Set-Volume -DriveLetter "D" -DedupMode Backup`
