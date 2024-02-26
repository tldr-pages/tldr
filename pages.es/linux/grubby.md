# grubby

> Herramienta para configurar los gestores de arranque `grub` y `zipl`.
> Más información: <https://manned.org/man/grubby.8>.

- Añade argumentos de arranque del kernel a todas las entradas del menú del kernel:

`sudo grubby --update-kernel=ALL --args '{{quiet console=ttyS0}}'`

- Elimina los argumentos existentes de la entrada para el kernel por defecto:

`sudo grubby --update-kernel=DEFAULT --remove-args {{quiet}}`

- Lista todas las entradas del menú del kernel:

`sudo grubby --info=ALL`
