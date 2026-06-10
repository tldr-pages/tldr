# VBoxManage startvm

> Գործարկել վիրտուալ մեքենա:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm>:.

- Սկսեք վիրտուալ մեքենա.:

`VBoxManage startvm {{vm_name|uuid}}`

- Գործարկեք վիրտուալ մեքենա նշված UI ռեժիմով.:

`VBoxManage startvm {{vm_name|uuid}} --type {{headless|gui|sdl|separate}}`

- Նշեք գաղտնաբառի ֆայլ՝ կոդավորված վիրտուալ մեքենա սկսելու համար.:

`VBoxManage startvm {{vm_name|uuid}} --password {{path/to/password_file}}`

- Նշեք գաղտնաբառի ID՝ գաղտնագրված վիրտուալ մեքենա սկսելու համար.:

`VBoxManage startvm {{vm_name|uuid}} --password-id {{password_id}}`

- Սկսեք վիրտուալ մեքենա շրջակա միջավայրի փոփոխական զույգի անվան արժեքով.:

`VBoxManage startvm {{vm_name|uuid}} {{[-E|--putenv]}} {{name}}={{value}}`
