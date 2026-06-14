# VBoxManage unregistervm

> Չգրանցել վիրտուալ մեքենա (VM):.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-unregistervm>:.

- Չեղարկել գոյություն ունեցող VM-ի գրանցումը.:

`VBoxManage unregistervm {{uuid|vm_name}}`

- Ջնջել կոշտ սկավառակի պատկերի ֆայլերը, բոլոր պահպանված վիճակի ֆայլերը, VM տեղեկամատյանները և XML VM մեքենայի ֆայլերը.:

`VBoxManage unregistervm {{uuid|vm_name}} --delete`

- Ջնջել բոլոր ֆայլերը VM-ից.:

`VBoxManage unregistervm {{uuid|vm_name}} --delete-all`
