# xml ցուցակ

> Ցուցակագրեք գրացուցակի բովանդակությունը (օրինակ՝ `ls`) XML ձևաչափով:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139535968>:.

- Ներկայիս գրացուցակի ցուցակը գրեք XML փաստաթղթում.:

`xml {{[ls|list]}} > {{path/to/dir_list.xml}}`

- Նշված գրացուցակի ցուցակը գրեք XML փաստաթղթում.:

`xml {{[ls|list]}} {{path/to/directory}} > {{path/to/dir_list.xml}}`

- Ցուցադրել օգնությունը.:

`xml {{[ls|list]}} --help`
