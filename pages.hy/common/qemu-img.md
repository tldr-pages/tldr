# qemu-img

> Ստեղծեք և շահարկեք Quick Emulator վիրտուալ HDD պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://qemu.readthedocs.io/en/master/tools/qemu-img.html>:.

- Ստեղծեք սկավառակի պատկեր որոշակի չափով (գիգաբայթերով).:

`qemu-img create {{path/to/image_file.img}} {{gigabytes}}G`

- Ցույց տալ տեղեկատվություն սկավառակի պատկերի մասին.:

`qemu-img info {{path/to/image_file.img}}`

- Բարձրացնել կամ նվազեցնել պատկերի չափը.:

`qemu-img resize {{path/to/image_file.img}} {{gigabytes}}G`

- Թափել նշված սկավառակի պատկերի յուրաքանչյուր հատվածի տեղաբաշխման վիճակը.:

`qemu-img map {{path/to/image_file.img}}`

- Փոխակերպեք VMware `.vmdk` սկավառակի պատկերը KVM `.qcow2` սկավառակի պատկերի և ցուցադրեք [p]առաջընթացը՝:

`qemu-img convert -f vmdk -O qcow2 -p {{path/to/image_file.vmdk}} {{path/to/image_file.qcow2}}`

- [c]ստեղծել KVM `.qcow2` սկավառակի ներքին պատկերը՝:

`qemu-img snapshot -c {{snapshot_tag_name}} {{path/to/image_file.qcow2}}`

- [a]կիրառեք ներքին պատկերը KVM `.qcow2` սկավառակի պատկերին՝:

`qemu-img snapshot -a {{snapshot_tag_name}} {{path/to/image_file.qcow2}}`
