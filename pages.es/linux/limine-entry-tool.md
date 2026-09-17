# limine-entry-tool

> Un script auxiliar para gestionar las entradas del gestor de arranque Limine en sistemas UEFI.
> Más información: <https://gitlab.com/Zesko/limine-entry-tool>.

- Busca otras entradas de arranque UEFI activas y las añade al menú de Limine:

`limine-entry-tool --scan`

- Añade una nueva entrada de arranque del kernel con un initramfs y un archivo de kernel:

`limine-entry-tool --add "{{nombre_kernel}}" "{{ruta/a/initramfs}}" "{{ruta/a/vmlinuz}}"`

- Añadir una nueva entrada de arranque de imagen de kernel unificada (UKI):

`limine-entry-tool --add-uki "{{nombre_kernel}}" "{{ruta/a/uki.efi}}"`

- Eliminar una entrada de arranque del kernel y sus archivos asociados del ESP:

`limine-entry-tool --remove "{{nombre_kernel}}"`

- Eliminar una entrada completa del sistema operativo por su nombre o ID de máquina:

`limine-entry-tool --remove-os "{{os_name|machine_id}}"`

- Añadir una entrada de arranque EFI para un gestor de arranque alternativo (por ejemplo, Windows):

`limine-entry-tool --add-efi "{{nombre_arranque_efi}}" "{{ruta/a/loader.efi}}"`
