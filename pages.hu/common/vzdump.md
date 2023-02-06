# vzdump

> Biztonsági mentési segédprogram virtuális gépekhez és konténerekhez. További információ: <https://pve.proxmox.com/pve-docs/vzdump.1.html>.

- A vendég virtuális gép mentése az alapértelmezett mentési könyvtárba (általában `/var/lib/vz/dump/`), kivéve a pillanatfelvételeket:

`vzdump {{vm_id}}`

- A 101, 102 és 103 azonosítóval rendelkező vendég virtuális gépek biztonsági mentése:

`vzdump {{101 102 103}}`

- Vendég virtuális gép dumpolása egy adott üzemmóddal:

`vzdump {{vm_id}} --mode {{suspend|snapshot}}`

- Biztonsági mentés az összes vendégrendszerről, és értesítő e-mail küldése a root és az admin felhasználóknak:

`vzdump --all --mode {{suspend}} --mailto {{root}} --mailto {{admin}}`

- Pillanatkép mód használata (nincs szükség leállási időre) és egy nem alapértelmezett dump könyvtár használata:

`vzdump {{vm_id}} --dumpdir {{path/to/directory}} --mode {{snapshot}}`

- Az összes vendég virtuális gép biztonsági mentése a 101-es és 102-es azonosító kivételével:

`vzdump --mode {{suspend}} --exclude {{101, 102}}`
