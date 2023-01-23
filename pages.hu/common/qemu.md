# qemu

> Általános gépemulátor és virtualizátor. Támogatja a CPU architektúrák széles skáláját. További információ: <https://www.qemu.org>.

- Indítás i386 architektúrát emuláló képből:

`qemu-system-i386 -hda {{image_name.img}}`

- Boot from image emulating x64 architecture:

`qemu-system-x86_64 -hda {{image_name.img}}`

- QEMU-példány indítása élő ISO-kép segítségével:

`qemu-system-i386 -hda {{image_name.img}} -cdrom {{os_image.iso}} -boot d`

- A példány RAM-mennyiségének megadása:

`qemu-system-i386 -m 256 -hda image_name.img -cdrom os-image.iso -boot d`

- Indítás fizikai eszközről (pl. USB-ről, hogy tesztelje a bootolható adathordozót):

`qemu-system-i386 -hda /dev/{{storage_device}}`
