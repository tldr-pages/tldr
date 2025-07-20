# Get-FileHash

> Calcula un hash para un archivo.
> Nota: Este comando solo se puede usar a través de PowerShell.
> Más información: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/get-filehash>.

- Calcula un hash para un archivo especificado utilizando el algoritmo SHA256:

`Get-FileHash {{ruta\al\archivo}}`

- Calcula un hash para un archivo especificado utilizando un algoritmo específico:

`Get-FileHash {{ruta\al\archivo}} -Algorithm {{SHA1|SHA384|SHA256|SHA512|MD5}}`
