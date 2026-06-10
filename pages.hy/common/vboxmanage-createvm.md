# VBoxManage createvm

> Ստեղծեք նոր վիրտուալ մեքենա:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-createvm>:.

- Ստեղծեք նոր VM լռելյայն կարգավորումներով.:

`VBoxManage createvm --name {{vm_name}}`

- Սահմանեք բազային թղթապանակը, որտեղ կպահվի VM-ի կոնֆիգուրացիան.:

`VBoxManage createvm --name {{vm_name}} --basefolder {{path/to/directory}}`

- Սահմանեք հյուրի ՕՀ-ի տեսակը (`VBoxManage list ostypes`-ից մեկը) ներմուծված VM-ի համար.:

`VBoxManage createvm --name {{vm_name}} --ostype {{ostype}}`

- Գրանցեք ստեղծված VM-ը VirtualBox-ում.:

`VBoxManage createvm --name {{vm_name}} --register`

- Սահմանեք VM-ը նշված խմբերին.:

`VBoxManage createvm --name {{vm_name}} --group {{group1,group2,...}}`

- Սահմանեք VM-ի համընդհանուր եզակի նույնացուցիչը (UUID).:

`VBoxManage createvm --name {{vm_name}} --uuid {{uuid}}`

- Սահմանեք ծածկագիրը՝ օգտագործելու համար կոդավորումը.:

`VBoxManage createvm --name {{vm_name}} --cipher {{AES-128|AES-256}}`
