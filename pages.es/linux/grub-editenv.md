# grub-editenv

> Edita las variables de entorno de GRUB.
> Más información: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- Establece una entrada de arranque por defecto (asumiendo que la entrada de arranque ya existe):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- Muestra todas las variables de entorno de GRUB:

`grub-editenv /boot/grub/grubenv list`

- Restablece la variable `saved_entry` al valor por defecto:

`grub-editenv /boot/grub/grubenv unset saved_entry`
