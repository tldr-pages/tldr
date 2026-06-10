# VBoxManage clonevm

> Ստեղծեք գոյություն ունեցող վիրտուալ մեքենայի (VM) կլոն:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-clonevm>:.

- Կլոնավորեք նշված VM-ը.:

`VBoxManage clonevm {{vm_name}}`

- Նշեք նոր անուն նոր VM-ի համար.:

`VBoxManage clonevm {{vm_name}} --name {{new_vm_name}}`

- Նշեք այն թղթապանակը, որտեղ պահպանված է VM-ի նոր կոնֆիգուրացիան.:

`VBoxManage clonevm {{vm_name}} --basefolder {{path/to/directory}}`

- Գրանցեք կլոնավորված VM-ը VirtualBox-ում.:

`VBoxManage clonevm {{vm_name}} --register`
