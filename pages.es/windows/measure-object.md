# Measure-Object

> Calcula las propiedades numéricas de los objetos, así como los caracteres, palabras y líneas en objetos de cadena, como archivos de texto.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/measure-object>.

- Cuenta los archivos y carpetas en un directorio:

`Get-ChildItem | Measure-Object`

- Pasa la entrada a Measure-Object (los objetos que se pasan a `Measure-Object` están disponibles para el bloque de script que se pasa al parámetro Expression):

`"Uno", "Dos", "Tres", "Cuatro" | Set-Content -Path "{{ruta\al\archivo}}"; Get-Content "{{ruta\al\archivo}}"; | Measure-Object -Character -Line -Word`
