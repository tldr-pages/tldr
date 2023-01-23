# trace-cmd

> Segédprogram az Ftrace Linux kernel belső nyomkövetőjével való interakcióhoz. Ez a segédprogram csak root felhasználóként fut. További információ: <https://manned.org/trace-cmd>.

- A nyomkövető rendszer állapotának megjelenítése:

`trace-cmd stat`

- Az elérhető nyomkövetők listája:

`trace-cmd list -t`

- Nyomkövetés indítása egy adott bővítménnyel:

`trace-cmd start -p {{timerlat|osnoise|hwlat|blk|mmiotrace|function_graph|wakeup_dl|wakeup_rt|wakeup|function|nop}}`

- A nyomkövetési kimenet megtekintése:

`trace-cmd show`

- A nyomkövetés leállítása, de a pufferek megtartása:

`trace-cmd stop`

- A nyomkövetési pufferek törlése:

`trace-cmd clear`

- A nyomkövetési pufferek törlése és a nyomkövetés leállítása:

`trace-cmd reset`
