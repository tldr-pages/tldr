# virsh pool-undefine

> A leállított virtuális gép tárolóállományának konfigurációs fájljának törlése a `/etc/libvirt/storage` oldalon. Lásd még: `virsh`, `virsh-pool-destroy`. További információ: [https://manned.org/virsh.](https://manned.org/virsh)

- Törli a konfigurációt a tárolómedence megadott nevére vagy UUID-jára (a `virsh pool-list` segítségével határozza meg):

`virsh pool-undefine --pool {{name|uuid}}`
