# choco source

> Gestiona fuentes para paquetes con Chocolatey.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/source/>.

- Listar las fuentes actualmente disponibles:

`choco source list`

- Agregar una nueva fuente de paquete:

`choco source add {{[-n|--name]}} {{nombre}} {{[-s|--source]}} {{url}}`

- Agregar una nueva fuente de paquete con credenciales:

`choco source add {{[-n|--name]}} {{nombre}} {{[-s|--source]}} {{url}} {{[-u|--user]}} {{nombre_usuario}} {{[-p|--password]}} {{contraseña}}`

- Agregar una nueva fuente de paquete con un certificado de cliente:

`choco source add {{[-n|--name]}} {{nombre}} {{[-s|--source]}} {{url}} --cert {{ruta\al\archivo_certificado}}`

- Habilitar una fuente de paquete:

`choco source enable {{[-n|--name]}} {{nombre}}`

- Deshabilitar una fuente de paquete:

`choco source disable {{[-n|--name]}} {{nombre}}`

- Eliminar una fuente de paquete:

`choco source remove {{[-n|--name]}} {{nombre}}`
