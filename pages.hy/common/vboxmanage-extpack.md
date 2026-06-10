# VBoxManage extpack

> Կառավարեք ընդլայնման փաթեթները Oracle VirtualBox-ի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-extpack>:.

- Տեղադրեք ընդլայնման փաթեթներ VirtualBox-ում (Նշում. նոր տարբերակ տեղադրելուց առաջ անհրաժեշտ է հեռացնել ընդլայնման փաթեթի առկա տարբերակը):

`VBoxManage extpack install {{path/to/file.vbox-extpack}}`

- Հեռացրեք VirtualBox ընդլայնման փաթեթի գոյություն ունեցող տարբերակը.:

`VBoxManage extpack install --replace`

- Տեղահանեք ընդլայնման փաթեթները VirtualBox-ից.:

`VBoxManage extpack uninstall {{extension_pack_name}}`

- Տեղահանեք ընդլայնման փաթեթները և բաց թողեք ապատեղադրման մերժումների մեծ մասը.:

`VBoxManage extpack uninstall --force {{extension_pack_name}}`

- Մաքրել ընդլայնման փաթեթների թողած ժամանակավոր ֆայլերը և գրացուցակները.:

`VBoxManage extpack cleanup`
