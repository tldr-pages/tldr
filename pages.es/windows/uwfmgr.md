# uwfmgr

> Unified Write Filter (UWF).
> Protege las unidades redirigiendo cualquier escritura a una superposición virtual. Las escrituras se descartan al reiniciar, a menos que se confirmen por defecto.
> Más información: <https://learn.microsoft.com/windows/iot/iot-enterprise/customize/unified-write-filter>.

- Obtener el estado actual:

`uwfmgr get-config`

- Establecer una unidad como protegida:

`uwfmgr volume protect {{letra_de_unidad}}:`

- Quitar una unidad de la lista de protección:

`uwfmgr volume unprotect {{letra_de_unidad}}:`

- Habilitar o deshabilitar la protección (se aplica después del reinicio):

`uwfmgr filter {{enable|disable}}`

- Confirmar los cambios de un archivo en una unidad protegida:

`uwfmgr file commit {{letra_de_unidad:\ruta\al\archivo}}`

- Confirmar la eliminación de un archivo en una unidad protegida:

`uwfmgr file commit-delete {{letra_de_unidad:\ruta\al\archivo}}`
