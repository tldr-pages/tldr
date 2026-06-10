# VBoxManage ներմուծում

> Ներմուծեք նախկինում արտահանված վիրտուալ մեքենա (VM):.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-import>:.

- Ներմուծեք VM OVF կամ OVA ֆայլից.:

`VBoxManage import {{path/to/file.ovf}}`

- Սահմանեք ներմուծված VM-ի անունը.:

`VBoxManage import {{path/to/file.ovf}} --name {{vm_name}}`

- Նշեք այն թղթապանակը, որտեղ կպահվի ներմուծված VM-ի կոնֆիգուրացիան.:

`VBoxManage import {{path/to/file.ovf}} --basefolder {{path/to/directory}}`

- Գրանցեք ներմուծված VM-ը VirtualBox-ում.:

`VBoxManage import {{path/to/file.ovf}} --register`

- Կատարեք չոր վազք՝ ստուգելու ներմուծումը առանց իրականում ներմուծելու.:

`VBoxManage import {{path/to/file.ovf}} --dry-run`

- Սահմանեք հյուրի ՕՀ-ի տեսակը (`VBoxManage list ostypes`-ից մեկը) ներմուծված VM-ի համար.:

`VBoxManage import {{path/to/file.ovf}} --ostype {{ostype}}`

- Սահմանեք հիշողությունը (մեգաբայթերով) ներմուծված VM-ի համար.:

`VBoxManage import {{path/to/file.ovf}} --memory {{1}}`

- Սահմանեք CPU-ների քանակը ներմուծված VM-ի համար.:

`VBoxManage import {{path/to/file.ovf}} --cpus {{1}}`
