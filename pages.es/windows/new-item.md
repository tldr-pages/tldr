# New-Item

> Crear un nuevo archivo, directorio, enlace simbólico o una entrada de registro.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.management/new-item>.

- Crear un nuevo archivo en blanco (equivalente a `touch`):

`New-Item {{ruta\al\archivo}}`

- Crear un nuevo directorio:

`New-Item -ItemType Directory {{ruta\al\directorio}}`

- Escribir un nuevo archivo de texto con el contenido especificado:

`New-Item {{ruta\al\archivo}} -Value {{contenido}}`

- Escribir el mismo archivo de texto en múltiples ubicaciones:

`New-Item {{ruta\al\archivo1 , ruta\al\archivo2 , ...}} -Value {{contenido}}`

- Crear un enlace simbólico\enlace duro\unión a un archivo o directorio:

`New-Item -ItemType {{SymbolicLink|HardLink|Junction}} -Path {{ruta\al\archivo_enlace}} -Target {{ruta\al\archivo_o_directorio_fuente}}`

- Crear una nueva entrada de registro en blanco (en REG_SZ, usar `New-ItemProperty` o `Set-ItemProperty` para ajustar el tipo de valor):

`New-Item {{ruta\al\clave_de_registro}}`

- Crear una nueva entrada de registro en blanco con un valor especificado:

`New-Item {{ruta\al\clave_de_registro}} -Value {{valor}}`
