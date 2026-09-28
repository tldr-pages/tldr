# Tee-Object

> Guarda la salida de un comando en un archivo o variable y también la envía por la tubería (pipeline).
> Nota: Este comando solo se puede usar en PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Guarda la lista de procesos en un archivo y la muestra en la consola:

`Get-Process | Tee-Object -FilePath {{ruta\al\archivo}}`

- Guarda el proceso "notepad" en una variable y luego selecciona propiedades específicas:

`Get-Process notepad | Tee-Object -Variable {{proceso}} | Select-Object processname,handles`
