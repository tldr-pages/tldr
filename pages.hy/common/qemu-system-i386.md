# qemu-system-i386

> Ընդօրինակել `i386` ճարտարապետությունը:.
> Լրացուցիչ տեղեկություններ. <https://www.qemu.org/docs/master/system/target-i386.html>:.

- Բացեք `i386` ճարտարապետությունը նմանակող պատկերից.:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}}`

- Գործարկեք QEMU օրինակ կենդանի ISO պատկերից.:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}} -cdrom {{os_image.iso}} -boot d`

- Բեռնում ֆիզիկական սարքից (օրինակ՝ USB-ից՝ bootable media փորձարկելու համար).:

`qemu-system-i386 -hda {{/dev/storage_device}} -m {{4096}}`

- Մի գործարկեք VNC սերվեր.:

`qemu-system-i386 -hda {{image_name.img}} -m {{4096}} -nographic`

- Ելք ոչ գրաֆիկական QEMU-ից.:

`<Ctrl a><x>`

- Թվարկեք աջակցվող մեքենաների տեսակները.:

`qemu-system-i386 {{[-M|-machine]}} help`
