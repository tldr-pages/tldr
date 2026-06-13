# Tee-Object

> Guarda la salida de un comando en un archivo o variable y también la envía por la tubería (pipeline).
> Nota: Este comando solo se puede usar en PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/tee-object>.

- Guardar la lista de procesos en un archivo y mostrarla en la consola:

`Get-Process | Tee-Object -FilePath {{ruta\al\archivo}}`

- Guardar el proceso "notepad" en una variable y luego seleccionar propiedades específicas:

`Get-Process notepad | Tee-Object -Variable {{proceso}} | Select-Object processname,handles`
