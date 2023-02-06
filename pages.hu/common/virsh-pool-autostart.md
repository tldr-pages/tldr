# virsh pool-autostart

> Az automatikus indítás engedélyezése vagy letiltása egy virtuális gép tárolóállományához. Lásd még: `virsh`. További információ: <https://manned.org/virsh>.

- Engedélyezze az automatikus indítást a név vagy UUID által megadott tárolómedence számára (meghatározás a `virsh pool-list` segítségével):

`virsh pool-autostart --pool {{name|uuid}}`

- Az automatikus indítás letiltása a név vagy UUID által megadott tárolómedence számára:

`virsh pool-autostart --pool {{name|uuid}} --disable`
