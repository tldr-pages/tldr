# repair-bde

> Intentar reparar o descifrar un volumen cifrado con BitLocker dañado.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/repair-bde>.

- Intentar reparar un volumen especificado:

`repair-bde {{C:}}`

- Intentar reparar un volumen especificado y enviar la salida a otro volumen:

`repair-bde {{C:}} {{D:}}`

- Intentar reparar un volumen especificado usando el archivo de clave de recuperación proporcionado:

`repair-bde {{C:}} -RecoveryKey {{ruta\al\archivo.bek}}`

- Intentar reparar un volumen especificado usando la contraseña numérica de recuperación proporcionada:

`repair-bde {{C:}} -RecoveryPassword {{contraseña}}`

- Intentar reparar un volumen especificado usando la contraseña proporcionada:

`repair-bde {{C:}} -Password {{contraseña}}`

- Intentar reparar un volumen especificado usando el paquete de claves proporcionado:

`repair-bde {{C:}} -KeyPackage {{ruta\al\directorio}}`

- Registrar toda la salida en un archivo específico:

`repair-bde {{C:}} -LogFile {{ruta\al\archivo}}`

- Mostrar ayuda:

`repair-bde /?`
