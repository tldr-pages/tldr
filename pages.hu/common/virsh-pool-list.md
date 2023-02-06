# virsh pool-list

> A virtuális gépek tárolócsoportjaira vonatkozó információk listázása. Lásd még: `virsh`, `virsh-pool-autostart`, `virsh-pool-define-as`. További információ: <https://manned.org/virsh>.

- Az aktív tárolómedencék nevének, állapotának és az automatikus indítás engedélyezve vagy letiltva van-e:

`virsh pool-list`

- Az aktív és inaktív vagy csak inaktív tárolómedencékre vonatkozó információk listázása:

`virsh pool-list --{{all|inactive}}`

- Kiterjesztett információk listázása a perzisztenciáról, a kapacitásról, a kiosztásról és a rendelkezésre álló helyről az aktív tárolómedencék esetében:

`virsh pool-list --details`

- Az automatikus indítás engedélyezve vagy letiltva lévő aktív tárolómedencék információinak listázása:

`virsh pool-list --{{autostart|no-autostart}}`

- A tartós vagy átmeneti aktív tárolócsoportok adatainak listázása:

`virsh pool-list --{{persistent|transient}}`

- Az aktív tárolómedencék nevének és UUID-jének listázása:

`virsh pool-list --name --uuid`
