# choco pin

> Fija un paquete en la versión escogida con Chocolatey.
> Los paquetes fijados se omiten automáticamente al actualizar.
> Más información: <https://chocolatey.org/docs/commands-pin>.

- Mostrar una lista de paquetes fijados y sus versiones:

`choco pin list`

- Fijar un paquete en su versión actual:

`choco pin add --name {{paquete}}`

- Fijar un paquete en una versión específica:

`choco pin add --name {{paquete}} --version {{versión}}`

- Eliminar un pin para un paquete específico:

`choco pin remove --name {{paquete}}`
