# msiexec

> Instalar, actualizar, reparar o desinstalar programas de Windows utilizando archivos de paquetes MSI y MSP.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/msiexec>.

- Instalar un programa desde su paquete MSI:

`msiexec /package {{ruta\al\archivo.msi}}`

- Instalar un paquete MSI desde un sitio web:

`msiexec /package {{https://ejemplo.com/instalador.msi}}`

- Instalar un archivo de parche MSP:

`msiexec /update {{ruta\al\archivo.msp}}`

- Desinstalar un programa o parche utilizando su respectivo archivo MSI o MSP:

`msiexec /uninstall {{ruta\al\archivo}}`
