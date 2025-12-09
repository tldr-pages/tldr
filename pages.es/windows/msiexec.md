# msiexec

> Instala, actualiza, repara o desinstala programas de Windows utilizando archivos de paquetes MSI y MSP.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Instala un programa desde su paquete MSI:

`msiexec /package {{ruta\al\archivo.msi}}`

- Instala un paquete MSI desde un sitio web:

`msiexec /package {{https://ejemplo.com/instalador.msi}}`

- Instala un archivo de parche MSP:

`msiexec /update {{ruta\al\archivo.msp}}`

- Desinstala un programa o parche utilizando su respectivo archivo MSI o MSP:

`msiexec /uninstall {{ruta\al\archivo}}`
