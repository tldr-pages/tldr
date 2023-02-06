# virsh pool-build

> A virtuális gép tárolóállományának alapjául szolgáló tárolórendszer létrehozása a virtuális gép konfigurációs fájljában meghatározottak szerint a `/etc/libvirt/storage` oldalon.
> Lásd még: `virsh`, `virsh-pool-define-as`, `virsh-pool-start`.
> További információ: <https://manned.org/virsh>.

- A név vagy UUID alapján megadott tárolómedence létrehozása (a `virsh pool-list` segítségével határozza meg):

`virsh pool-build --pool {{name|uuid}}`
