# virsh pool-start

> Egy korábban konfigurált, de inaktív virtuális gép tárolóállományának elindítása. Lásd még: `virsh` `virsh-pool-define-as` `virsh-pool-destroy` További információ: <https://manned.org/virsh>.

- Indítsa el a név vagy UUID alapján megadott tárolómedencét (a `virsh pool-list` segítségével határozza meg), és hozza létre az alapul szolgáló tárolórendszert, ha az nem létezik:

`virsh pool-start --pool {{name|uuid}} --build`
