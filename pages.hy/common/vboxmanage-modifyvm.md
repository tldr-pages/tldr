# VBoxManage modifyvm

> Փոխեք կարգավորումները դադարեցված վիրտուալ մեքենայի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-modifyvm>:.

- Վերանվանել VM-ը.:

`VBoxManage modifyvm {{uuid|vm_name}} --name {{new_name}}`

- Կարգավորել հիշողությունը և պրոցեսորը.:

`VBoxManage modifyvm {{uuid|vm_name}} --memory {{2048}} --cpus {{2}}`

- Միացնել հեռավոր ցուցադրումը (VRDE):

`VBoxManage modifyvm {{uuid|vm_name}} --vrde on`

- Միացնել նստաշրջանի ձայնագրումը.:

`VBoxManage modifyvm {{uuid|vm_name}} --recording on`
