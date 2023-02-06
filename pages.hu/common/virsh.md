# virsh

> Virsh vendégtartományok kezelése. (MEGJEGYZÉS: a 'guest_id' lehet a vendég azonosítója, neve vagy UUID-je). Néhány alparancsnak, mint például a `virsh list`, saját használati dokumentációja van. További információ: <https://libvirt.org/virshcmdref.html>.

- Csatlakozás egy hypervisor munkamenethez:

`virsh connect {{qemu:///system}}`

- Az összes tartomány listázása:

`virsh list --all`

- A vendég konfigurációs fájljának kiürítése:

`virsh dumpxml {{guest_id}} > {{path/to/guest.xml}}`

- Vendég létrehozása konfigurációs fájlból:

`virsh create {{path/to/config_file.xml}}`

- Vendég konfigurációs fájljának szerkesztése (a szerkesztő a $EDITOR paranccsal módosítható):

`virsh edit {{guest_id}}`

- Vendég indítása/újraindítása/leállítása/felfüggesztése/újraindítása:

`virsh {{command}} {{guest_id}}`

- A vendég aktuális állapotának mentése egy fájlba:

`virsh save {{guest_id}} {{filename}}`

- Folyamatban lévő vendég törlése:

`virsh destroy {{guest_id}} && virsh undefine {{guest_id}}`
