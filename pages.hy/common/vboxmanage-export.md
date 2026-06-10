# VBoxManage արտահանում

> Արտահանել վիրտուալ մեքենաները վիրտուալ սարքի (ISO) կամ ամպային ծառայության մեջ:.
> Լրացուցիչ տեղեկություններ. <https://www.virtualbox.org/manual/ch08.html#vboxmanage-export>:.

- Նշեք թիրախային OVA ֆայլը.:

`VBoxManage export --output {{path/to/file.ova}}`

- Արտահանել OVF 0.9 ժառանգական ռեժիմով.:

`VBoxManage export --legacy09`

- Արտահանել OVF (0.9|1.0|2.0) ձևաչափով.:

`VBoxManage export --{{ovf09|ovf10|ovf20}}`

- Ստեղծեք արտահանվող ֆայլերի մանիֆեստը.:

`VBoxManage export --manifest`

- Նշեք VM-ի նկարագրությունը.:

`VBoxManage export --description "{{vm_description}}"`
