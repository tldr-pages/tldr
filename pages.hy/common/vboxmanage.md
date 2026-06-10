# VBoxManage

> Ինտերֆեյս VirtualBox-ի հետ:.
> Ներառում է GUI-ի բոլոր գործառույթները և ավելին:.
> Որոշ ենթահրամաններ, ինչպիսիք են `startvm`-ն, ունեն իրենց օգտագործման փաստաթղթերը:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-intro>:.

- Թվարկեք բոլոր VirtualBox վիրտուալ մեքենաները.:

`VBoxManage list vms`

- Ցույց տալ տեղեկատվություն որոշակի վիրտուալ մեքենայի մասին.:

`VBoxManage showvminfo {{name|uuid}}`

- Սկսեք վիրտուալ մեքենա.:

`VBoxManage startvm {{name|uuid}}`

- Գործարկեք վիրտուալ մեքենա անգլուխ ռեժիմով.:

`VBoxManage startvm {{name|uuid}} --type headless`

- Անջատեք վիրտուալ մեքենան և պահպանեք դրա ներկայիս վիճակը.:

`VBoxManage controlvm {{name|uuid}} savestate`

- Անջատեք վիրտուալ մեքենան՝ առանց դրա վիճակը պահպանելու.:

`VBoxManage controlvm {{name|uuid}} poweroff`

- Թարմացրեք VBox ընդլայնման փաթեթները.:

`VBoxManage extpack install --replace {{VboxExtensionPackFileName}}`

- Ցուցադրել օգնությունը.:

`VBoxManage --help`
