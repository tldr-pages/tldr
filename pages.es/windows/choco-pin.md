# choco pin

> Fija un paquete en la versión escogida con Chocolatey.
> Los paquetes fijados se omiten automáticamente al actualizar.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/pin/>.

- Muestra una lista de paquetes fijados y sus versiones:

`choco pin list`

- Fija un paquete en su versión actual:

`choco pin add {{[-n|--name]}} {{paquete}}`

- Fija un paquete en una versión específica:

`choco pin add {{[-n|--name]}} {{paquete}} --version {{versión}}`

- Elimina un pin para un paquete específico:

`choco pin remove {{[-n|--name]}} {{paquete}}`
