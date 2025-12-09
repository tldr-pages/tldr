# choco source

> Gestiona fuentes para paquetes con Chocolatey.
> Más información: <https://chocolatey.org/docs/commands-source>.

- Listar las fuentes actualmente disponibles:

`choco source list`

- Agregar una nueva fuente de paquete:

`choco source add --name {{nombre}} --source {{url}}`

- Agregar una nueva fuente de paquete con credenciales:

`choco source add --name {{nombre}} --source {{url}} --user {{nombre_usuario}} --password {{contraseña}}`

- Agregar una nueva fuente de paquete con un certificado de cliente:

`choco source add --name {{nombre}} --source {{url}} --cert {{ruta\al\archivo_certificado}}`

- Habilitar una fuente de paquete:

`choco source enable --name {{nombre}}`

- Deshabilitar una fuente de paquete:

`choco source disable --name {{nombre}}`

- Eliminar una fuente de paquete:

`choco source remove --name {{nombre}}`
