# zpool

> Gestionați bazine ZFS.

- Afișați configurația și starea tuturor zpools ZFS:

`zpool status`

- Verificați un bazin ZFS pentru erori (verifică suma de control a fiecărui bloc). Foarte intensiv CPU și disc:

`zpool scrub {{pool_name}}`

- Lista zpool disponibile pentru import:

`zpool import`

- Import un zpool:

`zpool import {{pool_name}}`

- Exportați un zpool (demontați toate sistemele de fișiere):

`zpool export {{pool_name}}`

- Afișați istoricul tuturor operațiunilor de piscină:

`zpool history {{pool_name}}`

- Creați o piscină în oglindă:

`zpool create {{pool_name}} mirror {{disk1}} {{disk2}} mirror {{disk3}} {{disk4}}`

- Adăugați un dispozitiv cache (L2ARC) la un zpool:

`zpool add {{pool_name}} cache {{cache_disk}}`
