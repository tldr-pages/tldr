# abroot

> Utilidad que proporciona completa inmutabilidad y atomicidad mediante transacciones entre 2 estados de partición de la raíz (A⟺B).
> Las actualizaciones se realizan utilizando imágenes OCI, para asegurar que el sistema está siempre en un estado consistente.
> Más información: <https://github.com/Vanilla-OS/ABRoot>.

- Añade paquetes a la imagen local (Nota: después de ejecutar este comando, se necesita aplicar estos cambios):

`sudo abroot pkg add {{paquete}}`

- Elimina paquetes de la imagen local (Nota: después de ejecutar este comando, debe aplicar estos cambios):

`sudo abroot pkg remove {{paquete}}`

- Lista paquetes en la imagen local:

`sudo abroot pkg list`

- Aplica los cambios en la imagen local (Nota: es necesario reiniciar el sistema para que estos cambios sean aplicados):

`sudo abroot pkg apply`

- Retrocede su sistema al estado anterior:

`sudo abroot rollback`

- Edita/Visualiza los parámetros del kernel:

`sudo abroot kargs {{edit|show}}`

- Muestra estado:

`sudo abroot status`

- Muestra ayuda:

`abroot --help`
