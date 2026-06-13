# schroot

> Ejecuta un comando o inicia una interfaz interactiva de comando con un directorio raíz diferente. Más personalizable que `chroot`.
> Más información: <https://wiki.debian.org/Schroot>.

- Lista chroots disponibles:

`schroot --list`

- Ejecuta un comando en un chroot específico:

`schroot --chroot {{chroot}} {{comando}}`

- Ejecuta un comando con opciones en un chroot específico:

`schroot --chroot {{chroot}} {{comando}} -- {{opciones_de_comando}}`

- Ejecuta un comando en todos los chroots disponibles:

`schroot --all {{comando}}`

- Inicia una shell interactiva dentro de un chroot específico como usuario específico:

`schroot --chroot {{chroot}} --user {{usuario}}`

- Inicia una nueva sesión (devuelve un identificador único en `stdout`):

`schroot --begin-session --chroot {{chroot}}`

- Se conecta a una sesión existente:

`schroot --run-session --chroot {{id_de_sesión}}`

- Finaliza una sesión en curso:

`schroot --end-session --chroot {{id_de_sesión}}`
