# modprobe

> Añade o elimina módulos del núcleo Linux.
> Vea también: `kmod`, para otros comandos de gestión de módulos.
> Más información: <https://manned.org/modprobe>.

- Finge cargar un módulo en el kernel, pero no lo hace realmente:

`sudo modprobe --dry-run {{nombre_del_módulo}}`

- Carga un módulo en el kernel:

`sudo modprobe {{nombre_del_módulo}}`

- Elimina un módulo del núcleo:

`sudo modprobe --remove {{nombre_del_módulo}}`

- Elimina un módulo y los que dependen de él desde el núcleo:

`sudo modprobe {{[-r|--remove]}} --remove-holders {{nombre_del_módulo}}`

- Muestra las dependencias de un módulo del kernel:

`sudo modprobe --show-depends {{nombre_del_módulo}}`
