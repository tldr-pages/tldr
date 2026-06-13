# grub-file

> Verifica si un archivo es de un tipo de imagen arrancable.
> Más información: <https://manned.org/grub-file>.

- Verifica si un archivo es una imagen ARM EFI:

`grub-file --is-arm-efi {{ruta/al/archivo}}`

- Verifica si un archivo es una imagen i386 EFI:

`grub-file --is-i386-efi {{ruta/al/archivo}}`

- Verifica si un archivo es una imagen x86_64 EFI:

`grub-file --is-x86_64-efi {{ruta/al/archivo}}`

- Verifica si un archivo es una imagen ARM (kernel de Linux):

`grub-file --is-arm-linux {{ruta/al/archivo}}`

- Verifica si un archivo es una imagen x86 (kernel de Linux):

`grub-file --is-x86-linux {{ruta/al/archivo}}`

- Verifica si un archivo es una imagen x86_64 XNU (kernel de macOS):

`grub-file --is-x86_64-xnu {{ruta/al/archivo}}`
