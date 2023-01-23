# virsh pool-define-as

> Konfigurációs fájl létrehozása a `/etc/libvirt/storage` címen egy állandó virtuális gép tárolóállományához a megadott argumentumokból. Lásd még: `virsh`, `virsh-pool-build`, `virsh-pool-start`. További információ: <https://manned.org/virsh>.

- Létrehozza a pool_név nevű tárolómedence konfigurációs fájlját a `/var/vms` mint alapul szolgáló tárolórendszer használatával:

`virsh pool-define-as --name {{pool_name}} --type {{dir}} --target {{/var/vms}}`
