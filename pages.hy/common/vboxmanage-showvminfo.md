# VBoxManage showvminfo

> Ցույց տալ տեղեկատվություն գրանցված վիրտուալ մեքենայի մասին:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-showvminfo>:.

- Ցույց տալ տեղեկատվություն որոշակի վիրտուալ մեքենայի մասին.:

`VBoxManage showvminfo {{vm_name|uuid}}`

- Ցույց տալ ավելի մանրամասն տեղեկատվություն որոշակի վիրտուալ մեքենայի մասին.:

`VBoxManage showvminfo --details {{vm_name|uuid}}`

- Ցույց տալ տեղեկատվությունը մեքենայական ընթեռնելի ձևաչափով.:

`VBoxManage showvminfo --machinereadable {{vm_name|uuid}}`

- Նշեք գաղտնաբառը ID-ն, եթե վիրտուալ մեքենան գաղտնագրված է.:

`VBoxManage showvminfo --password-id {{password_id}} {{vm_name|uuid}}`

- Նշեք գաղտնաբառի ֆայլը, եթե վիրտուալ մեքենան գաղտնագրված է.:

`VBoxManage showvminfo --password {{path/to/password_file}} {{vm_name|uuid}}`

- Ցույց տալ որոշակի վիրտուալ մեքենայի տեղեկամատյանները.:

`VBoxManage showvminfo --log {{vm_name|uuid}}`
