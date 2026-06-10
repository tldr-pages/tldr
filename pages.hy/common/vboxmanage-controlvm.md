# VBoxManage controlvm

> Փոխեք ներկայումս գործող վիրտուալ մեքենայի վիճակը և կարգավորումները:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-controlvm>:.

- Ժամանակավորապես դադարեցնել վիրտուալ մեքենայի կատարումը.:

`VBoxManage controlvm {{uuid|vm_name}} pause`

- Վերսկսեք դադարեցված վիրտուալ մեքենայի կատարումը.:

`VBoxManage controlvm {{uuid|vm_name}} resume`

- Կատարեք սառը վերականգնում վիրտուալ մեքենայի վրա.:

`VBoxManage controlvm {{uuid|vm_name}} reset`

- Անջատեք վիրտուալ մեքենան նույն էֆեկտով, ինչ համակարգչի հոսանքի մալուխը քաշելը.:

`VBoxManage controlvm {{uuid|vm_name}} poweroff`

- Անջատեք վիրտուալ մեքենան և պահպանեք դրա ներկայիս վիճակը.:

`VBoxManage controlvm {{uuid|vm_name}} savestate`

- Ուղարկեք ACPI (Ընդլայնված կոնֆիգուրացիա և էներգիայի միջերես) անջատման ազդանշան վիրտուալ մեքենային.:

`VBoxManage controlvm {{uuid|vm_name}} acpipowerbutton`

- Հյուր OS-ին ինքն իրեն վերագործարկելու հրաման ուղարկեք.:

`VBoxManage controlvm {{uuid|vm_name}} reboot`

- Անջատեք վիրտուալ մեքենան՝ առանց դրա վիճակը պահպանելու.:

`VBoxManage controlvm {{uuid|vm_name}} shutdown`
