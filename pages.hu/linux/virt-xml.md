# virt-xml

> A libvirt Domain XML fájlok szerkesztése explicit parancssori opciókkal. MEGJEGYZÉS: a 'domain' a meglévő VM-ek nevére, UUID-jára vagy ID-jára utal (Lásd: tldr virsh). További információ: <https://github.com/virt-manager/virt-manager/blob/main/man/virt-xml.rst>.

- Egy adott opció összes alopciójának listázása:

`virt-xml --{{option}}=?`

- A lemez, a hálózat és a rendszerindítás összes alopciójának listázása:

`virt-xml --disk=? --network=? --boot=?`

- Egy adott tartomány értékének szerkesztése:

`virt-xml {{domain}} --edit --{{option}} {{suboption}}={{new_value}}`

- Egy adott tartomány leírásának módosítása:

`virt-xml {{domain}} --edit --metadata description="{{new_description}}"`

- A rendszerindító eszköz menü engedélyezése/letiltása egy adott tartományhoz:

`virt-xml {{domain}} --edit --boot bootmenu={{on|off}}`

- Gazdai USB hub csatlakoztatása egy futó VM-hez (lásd: tldr lsusb):

`virt-xml {{domain}} --update --add-device --hostdev {{bus}}.{{device}}`
