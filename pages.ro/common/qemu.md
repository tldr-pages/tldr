# qemu

> Emulator de mașini generice și virtualizator.
> Suportă o mare varietate de arhitecturi CPU.
> Mai multe informaţii: <https://www.qemu.org>

- Boot din imaginea emulând arhitectura i386:

`qemu-system-i386 -hda {{image_name.img}}`

- Boot de la arhitectura x64 emulatoare imagine:

`qemu-system-x86_64 -hda {{image_name.img}}`

- Boot instanță QEMU cu o imagine ISO live:

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d`

- Specificați cantitatea de memorie RAM, de exemplu:

`qemu-system-i386 -m 256 -hda image_name.img -cdrom os-image.iso -boot d`

- Boot de la dispozitivul fizic (de exemplu, de la USB pentru a testa mediul bootabil):

`qemu-system-i386 -hda /dev/{{storage_device}}`
