# VBoxManage registervm

> Գրանցեք վիրտուալ մեքենա (VM):.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-registervm>:.

- Գրանցեք գոյություն ունեցող VM.:

`VBoxManage registervm {{path/to/file.vbox}}`

- Տրամադրել VM-ի կոդավորման գաղտնաբառի ֆայլը.:

`VBoxManage registervm {{path/to/file.vbox}} --password {{path/to/password_file}}`

- Հրամանի տողում գաղտնագրման գաղտնաբառի հուշում.:

`VBoxManage registervm {{path/to/file.vbox}} --password -`
